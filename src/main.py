from core import Olx
from time import time
import requests

if __name__ == "__main__":

    olx = Olx("https://rs.olx.com.br/regioes-de-porto-alegre-torres-e-santa-cruz-do-sul/centro/imoveis/venda/apartamentos")
    olx.work()