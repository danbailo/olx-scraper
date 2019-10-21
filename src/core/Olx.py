from multiprocessing.pool import ThreadPool
from bs4 import BeautifulSoup
import xlsxwriter
import requests
import json
import re
import os

class Olx:
    def __init__(self, base_url, sheet):
        if base_url[:8] != "https://":
            base_url = "https://" + base_url
        if re.match(r"(https\:\/\/www\.olx\.com\.br\/$)|(https\:\/\/www\.olx\.com\.br$)", base_url):
            print('\nO link deve conter algum tópico de pesquisa, exemplo: "https://www.olx.com.br/imoveis"')
            exit(-1)        
        if not re.match(r".*(olx\.com\.br)", base_url):
            print("\nPor favor, insira um link da OLX, onde este deve conter alguma pesquisa!")
            exit(-1)
        if re.match(r"https:\/\/m.olx",base_url):
            base_url = re.sub(r"\&o=\d+","",base_url)
            self.__pattern_mobile = re.compile(r"(.*?p\&)(.*)")
            mobile_match = self.__pattern_mobile.match(base_url)
            self.mobile_url = mobile_match[1]+"o=@@@&"+mobile_match[2]
            self.base_url = False
        else:            
            self.base_url = re.sub(r"\?o\=\d+","",base_url)+"?o="
            self.mobile_url = False
        self.__ad_link = {}
        self.__user_phone = {}
        self.__pattern_all = re.compile(r".*")      
        self.__patern_cel = re.compile(r"\d{2}(9)\d{8}")
        self.no_number = 0
        if sheet[-5:] != ".xlsx":
            self.__sheet = sheet+".xlsx"
        else: self.__sheet = sheet
        

    def handler_ads(self,i):
        try:
            if not self.mobile_url:
                response = requests.get(self.base_url+str(i))
            else:
                url = self.mobile_url
                response = requests.get(re.sub(r"@@@",str(i),url))
            if response.status_code != 200: return False
            response.close()
        except Exception:
            return False
        soup = BeautifulSoup(response.text,"html.parser")                
        if not self.mobile_url:
            ad_list = soup.find(name="div",attrs={"class":"section_OLXad-list"})
            for ad in ad_list.findAll("a"):
                self.__ad_link[ad["id"]] = ad["href"]
        else:
            ad_list = soup.find(name="ul",attrs={"id":"main-ad-list"})
            for ad in ad_list.findAll("a"):
                id_ad = ad["href"].split("-")[-1]
                self.__ad_link[id_ad] = ad["href"]            

    def get_ads(self):
        pool = ThreadPool(10)
        list(pool.imap(self.handler_ads, list(range(1,101))))
 
    def handler_user(self,ad):
        try:
            response = requests.get(ad)
            if response.status_code != 200: return False
            response.close()
        except Exception: return False            
        soup = BeautifulSoup(response.text, "html.parser")
        script_data = soup.find("script",attrs={"data-json":self.__pattern_all})
        data = json.loads(script_data.get("data-json"))
        if data["ad"]["phone"]["phone"] != '':
            self.__user_phone[data["ad"]["user"]["userId"]] = data["ad"]["phone"]["phone"]
        else: self.no_number += 1

    def get_user(self):
        pool = ThreadPool(32)
        list(pool.imap(self.handler_user, list(self.__ad_link.values())))

    def write_sheet(self):
        workbook = xlsxwriter.Workbook(os.path.join("..","output",self.__sheet))
        worksheet = workbook.add_worksheet()

        phones_values = list(self.__user_phone.values())
        phones = [phone for phone in phones_values if phone != '']

        for row_number, phone_number in enumerate(phones):
            match_phone = self.__patern_cel.match(phone_number)
            if match_phone:
                phone_number = re.sub(match_phone[1],"",phone_number, count=1)            
            worksheet.write(row_number, 0, int(phone_number))
        workbook.close()
    
    def work(self):
        print("\nColetando anúncios...")
        self.get_ads()
        print("{len_ads} anúncios foram coletados com sucesso!\n".format(len_ads=len(self.__ad_link)))
        print("Coletando números de telefones dos anunciantes...")
        self.get_user()
        print("Foram identificados {total} anunciantes!".format(total=len(self.__user_phone)+self.no_number))
        print("{no_number} anunciantes não tinham número de telefone cadastrado.".format(no_number=self.no_number))
        print("{len_phone} números de telefone coletados com sucesso!\n".format(len_phone=len(self.__user_phone)))
        self.write_sheet()
        print("Os números foram gravados na planilha {sheet} com sucesso!".format(sheet=self.__sheet))
