import argparse

def get_args():
	parser=argparse.ArgumentParser(
		prog="main.py",
		description="Coleta os números de telefones dos anunciantes da OLX de uma determinada pesquisa."
	)
	parser.add_argument("-l","--link",
		type=str,
        required=True,
		help="Link da pesquisa da OLX. Em caso de dúvidas, leia o arquivo README.md",
	)
	parser.add_argument("-s","--sheet",
		type=str,
        required=False,
		default="Números.xlsx",
		help="Nome da planilha que serão gravados os números. Em caso de dúvidas, leia o arquivo README.md",
	)			
	return parser.parse_args()