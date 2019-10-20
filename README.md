# Scraper OLX

## Descrição
Este projeto consiste em coletar os números de telefone dos usuários que anunciaram determinado produto a partir do link da pesquisa do mesmo e os telefones destes usuários são gravados numa planilha Excel dentro do diretório `/output/`.

---
## Requisitos
* `Python - versão 3.7` - [Download](https://www.python.org/ftp/python/3.7.3/python-3.7.3-amd64.exe)
* `pip (Gerenciador de pacotes do Python)`

---
## Dependências

Para instalar as dependências, execute o comando abaixo num terminal/power sheel/prompt de comando de comando:

* `python -m pip install -r requirements.txt --user`

---
## Como usar

Para executar o programa, abra um terminal/power sheel/prompt de comando e como parâmetro de execução do mesmo é preciso passar o link da pesquisa que foi realizada na OLX e como parâmetro opcional, você pode escolher o nome da planilha que será gravado os números.:

* `cd src/`
* **Comando para exibir ajuda**
    * `python main.py -h`
* **Executa o programa coletando os números dos usuário que publicaram no seguinte link "https://sp.olx.com.br/sao-paulo-e-regiao/centro/imoveis/venda/apartamentos":**

    *Obs: Os links devem ser passados como parâmetro dentro de aspas duplas "AQUI"*
    
    * `python main.py --link "https://sp.olx.com.br/sao-paulo-e-regiao/centro/imoveis/venda/apartamentos"` 
    

Neste caso, como não foi passado nenhum parâmetro para o nome da planilha, a mesma será gravada como `Números.xlsx`

* **Executa o programa da mesma forma, mas agora a planilha será salva como `telefone.xlsx`**

    * `python main.py --link "https://sp.olx.com.br/sao-paulo-e-regiao/centro/imoveis/venda/apartamentos" --sheet telefone`

* **Exemplo coletando os dados a partir do link de uma pesquisa feita por um dispotivo mobile**

    * `python main.py --l "https://m.olx.com.br/busca?ca=51_s&cg=1001&f=p&q=Apartamento&w=1" -s mobile.xlsx`

O parâmetro de link pode ser usado de duas formas, `--link` ou `-l`.

O parâmetro de planilha pode ser usado de duas formas, `--sheet` ou `-s`.

Em ambos os casos, terão o mesmo efeito. O usuário pode também passar o nome da planilha como `nome.xlsx`, em vez de somente `nome`, porém, o efeito será o mesmo.

---