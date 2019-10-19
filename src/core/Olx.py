from bs4 import BeautifulSoup
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

    def __get_ads(self):
        ad_link = {}
        for i in range(1,101):
            response = requests.get(self.base_url+str(i))
            soup = BeautifulSoup(response.text,"html.parser")
            ad_list = soup.find(name="div",attrs={"class":"section_OLXad-list"})
            for ad in ad_list.findAll("a"):
                ad_link[ad["id"]] = ad["href"]
        return ad_link

    def get_request(self):
        user_info = {}
        for ad in self.__get_ads().values():
            response = requests.get(ad)
            soup = BeautifulSoup(response.text, "html.parser")
            script = soup.find("script",attrs={"data-json":re.compile(".*")})
            data = json.loads(script.get("data-json"))
            user_info[data["ad"]["user"]["userId"]] = [data["ad"]["user"]["name"],data["ad"]["phone"]["phone"]]
        return user_info
