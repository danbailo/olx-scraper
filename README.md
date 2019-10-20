# Scraper OLX

## Descrição
Este projeto consiste em coletar os números de telefone dos usuários que anunciaram determinado produto a partir do link da pesquisa do mesmo e os telefones destes usuários são gravados numa planilha Excel dentro do diretório `/output/`.

---
## Requisitos

* `Python - versão 3.7`
* `pip (Gerenciador de pacotes do Python)`

---
## Dependências

Para instalar as dependências, execute o comando abaixo num terminal/prompt de comando:

* `python -m pip install -r requirements.txt --user`

---
## Como usar

Para executar o programa, abra um terminal/prompt de comando e como parâmetro de execução do mesmo é preciso passar o link da pesquisa que foi realizada na OLX e como parâmetro opcional, você pode escolher o nome da planilha que será gravado os números.:

* `cd src/`
* **Comando para ajuda**
    * `python main.py -h`
* **Executa o programa coletando os números dos usuário que publicaram no seguinte link "https://sp.olx.com.br/sao-paulo-e-regiao/centro/imoveis/venda/apartamentos":**
    
    * `python main.py --link https://sp.olx.com.br/sao-paulo-e-regiao/centro/imoveis/venda/apartamentos`
       

Neste caso, como não foi passado nenhum parâmetro para o nome da planilha, a mesma será gravada como `Números.xlsx`

* **Executa o programa da mesma forma, mas agora a planilha será salva como `telefone.xlsx`**

    * `python main.py --link https://sp.olx.com.br/sao-paulo-e-regiao/centro/imoveis/venda/apartamentos --sheet telefone`

O parâmetro de link pode ser usado de duas formas, `--link` ou `-l`.

O parâmetro de planilha pode ser usado de duas formas, `--sheet` ou `-s`.

Em ambos os casos, terão o mesmo efeito. O usuário pode também passar o nome da planilha como `telefone.xlsx`, em vez de somente `telefone`, porém, o efeito será o mesmo.

---