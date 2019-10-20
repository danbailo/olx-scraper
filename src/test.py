import requests
from bs4 import BeautifulSoup
import re

i = 1

url = "https://m.olx.com.br/busca?ca=51_s&cg=1001&f=p&o=@@@&q=Apartamento&w=1"

response = requests.get(re.sub(r"@@@",str(i),url))
soup = BeautifulSoup(response.text, "html.parser")

frame = soup.find("ul", attrs={"id":"main-ad-list"})
for link in frame.findAll("a"):
    print(link["href"].split("-")[-1])