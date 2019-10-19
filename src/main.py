from core import Olx
from time import time
import requests

if __name__ == "__main__":

    olx = Olx("https://rs.olx.com.br/regioes-de-porto-alegre-torres-e-santa-cruz-do-sul/centro/imoveis/venda/apartamentos")
 

    # start = time()
    # olx.get_ads()
    # print(time()-start)

    # start = time()
    # olx.get_request()
    # print(time()-start)

    print(requests.get("https://apigw.olx.com.br/store/v1/accounts/ads/406403618").json()["fullName"])