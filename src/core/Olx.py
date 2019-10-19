from bs4 import BeautifulSoup
import requests

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
    def __init__(self, id_ad):
        self.__links = {
            "https://ac.olx.com.br/imoveis",
            "https://es.olx.com.br/imoveis",
            "https://pb.olx.com.br/imoveis",
            "https://ro.olx.com.br/imoveis",
            "https://al.olx.com.br/imoveis",
            "https://go.olx.com.br/imoveis",
            "https://pr.olx.com.br/imoveis",
            "https://rr.olx.com.br/imoveis",
            "https://ap.olx.com.br/imoveis",
            "https://ma.olx.com.br/imoveis",
            "https://pe.olx.com.br/imoveis",
            "https://sc.olx.com.br/imoveis",
            "https://am.olx.com.br/imoveis",
            "https://mt.olx.com.br/imoveis",
            "https://pi.olx.com.br/imoveis",
            "https://sp.olx.com.br/imoveis",
            "https://ba.olx.com.br/imoveis",
            "https://ms.olx.com.br/imoveis",
            "https://rj.olx.com.br/imoveis",
            "https://se.olx.com.br/imoveis",
            "https://ce.olx.com.br/imoveis",
            "https://mg.olx.com.br/imoveis",
            "https://rn.olx.com.br/imoveis",
            "https://to.olx.com.br/imoveis",
            "https://df.olx.com.br/imoveis",
            "https://pa.olx.com.br/imoveis",
            "https://rs.olx.com.br/imoveis"       
        }
