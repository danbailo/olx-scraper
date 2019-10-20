from multiprocessing.pool import ThreadPool
from bs4 import BeautifulSoup
import xlsxwriter
import requests
import json
import re

#ID_ANUNCIO = 675914491
#https://apigw.olx.com.br/store/v1/accounts/ads/ID_ANUNCIO

#uma forma de fazer é ir coletando todos os links e add num dict, onde a chave seria o id do anuncio
#e o valor seria a url pra ir pro anuncio

#a cada request, serao outras postagens, logo, o q da pra fazer e deixar rodando por mto tempo
#pra ficar coletando diversos anuncios e depois fazer um crawler pra acessar cada link e pegar os dados do anunciante

#depois de coletar por 


#COLETAR LINK DOS ANUNCIOS
#https://ms.olx.com.br/mato-grosso-do-sul/imoveis/2-pecas-e-um-banheiro-675941635

# response = requests.get("https://ms.olx.com.br/mato-grosso-do-sul/imoveis/apartamento-sobrado-estilo-kitnet-675918225")
# soup = BeautifulSoup(response.text, "html.parser")
# script = soup.find("script",attrs={"data-json":re.compile(".*")})
# data = json.loads(script.get("data-json"))
# print(data.keys())
# print(data["ad"]["phone"])

class Olx:
    def __init__(self, base_url):
        self.base_url = base_url+"?o="
        self.__ad_link = {}
        self.__user_phone = {}
        self.__pattern_all = re.compile(r".*")      
        self.__patern_cel = re.compile(r"\d{2}(9)\d{8}")
        self.__sheet = "Números.xlsx"

    def handler_ads(self,i):
        response = requests.get(self.base_url+str(i))
        response.close()
        soup = BeautifulSoup(response.text,"html.parser")
        ad_list = soup.find(name="div",attrs={"class":"section_OLXad-list"})
        for ad in ad_list.findAll("a"):
            self.__ad_link[ad["id"]] = ad["href"]

    def get_ads(self):
        pool = ThreadPool(10)
        list(pool.imap(self.handler_ads, list(range(1,101))))
        # print(list(self.__ad_link.items()))
 
    def handler_user(self,ad):
        response = requests.get(ad[1])
        response.close()
        soup = BeautifulSoup(response.text, "html.parser")
        script_data = soup.find("script",attrs={"data-json":self.__pattern_all})
        data = json.loads(script_data.get("data-json"))
        self.__user_phone[data["ad"]["user"]["userId"]] = data["ad"]["phone"]["phone"]

    def get_user(self):
        pool = ThreadPool(32)
        list(pool.imap(self.handler_user, list(self.__ad_link.items())))
        # print(*self.__user_phone.items(),sep="\n")

    def write_sheet(self):
        workbook = xlsxwriter.Workbook(self.__sheet)
        worksheet = workbook.add_worksheet()
        phone = list(self.__user_phone.values())
        for i in range(len(phone)):
            if repr(phone[i]) == '': continue
            match_phone = self.__patern_cel.match(phone[i])
            if match_phone:
                phone[i] = re.sub(match_phone[1],"",phone[i], count=1)            
            worksheet.write(i, 0, phone[i])
        workbook.close()
    
    def work(self):
        print("Coletando anúncios...")
        self.get_ads()
        print("{len_ads} anúncios foram coletados com sucesso!\n".format(len_ads=len(self.__ad_link)))
        print("Coletando números de telefones dos anunciantes...")
        self.get_user()
        print("{len_phone} números de telefone coletados com sucesso!\n".format(len_phone=len(self.__user_phone)))
        self.write_sheet()
        print("Os números foram escritos na planilha {sheet} com sucesso!".format(sheet=self.__sheet))
