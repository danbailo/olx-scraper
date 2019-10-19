from bs4 import BeautifulSoup
from multiprocessing.pool import ThreadPool
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
        self.__names = {}
        self.__user_info = {}

    def handler_ad(self,i):
        response = requests.get(self.base_url+str(i))
        soup = BeautifulSoup(response.text,"html.parser")
        ad_list = soup.find(name="div",attrs={"class":"section_OLXad-list"})
        for ad in ad_list.findAll("a"):
            self.__ad_link[ad["id"]] = [ad["href"]]

    def get_ads(self):
        pool = ThreadPool(10)
        list(pool.imap(self.handler_ad, list(range(1,101))))
        # print(list(self.__ad_link.items()))

    def handler_names(self, ad):
        response = requests.get("https://apigw.olx.com.br/store/v1/accounts/ads/"+ad).json()
        try:
            self.__names[ad] = response["fullName"]
        except Exception: pass
    
    def get_names(self):
        self.get_ads()
        pool = ThreadPool(32)
        list(pool.imap(self.handler_names, list(self.__ad_link.keys())))
        print(*self.__names.items(),sep="\n")
        print(len(self.__names))

    def handler_user(self,ad):
        response = requests.get(ad[1])
        soup = BeautifulSoup(response.text, "html.parser")
        script = soup.find("script",attrs={"data-json":re.compile(".*")})
        data = json.loads(script.get("data-json"))
        self.__user_info[data["ad"]["user"]["userId"]] = [data["ad"]["user"]["name"],data["ad"]["phone"]["phone"]]        

    def get_request(self):
        self.get_ads()
        pool = ThreadPool(32)
        list(pool.imap(self.handler_user, list(self.__ad_link.items())))
        print(*self.__user_info.items(),sep="\n")