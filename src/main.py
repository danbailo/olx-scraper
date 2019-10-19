from core import Olx
from time import time

if __name__ == "__main__":

    olx = Olx("https://rs.olx.com.br/regioes-de-porto-alegre-torres-e-santa-cruz-do-sul/centro/imoveis/venda/apartamentos")
    start = time()

    ads = olx.get_ads()
    print(*ads.items(), sep="\n")
    print(len(ads))
    print(time()-start)