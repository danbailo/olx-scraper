from bs4 import BeautifulSoup
import re
import requests
import json

if __name__ == "__main__":
    response = requests.get("https://ms.olx.com.br/mato-grosso-do-sul/imoveis/apartamento-sobrado-estilo-kitnet-675918225")
    soup = BeautifulSoup(response.text, "html.parser")
    script = soup.find("script",attrs={"data-json":re.compile(".*")})
    data = json.loads(script.get("data-json"))
    print(data.keys())
    print(data["ad"]["phone"])