from pandas import read_excel
import xlsxwriter
import args
import os

def join_all_xlsx(directory):
	all_xlsx = [os.path.join(directory,xlsx) for xlsx in os.listdir(directory) if xlsx[-5:] == ".xlsx"]
	return all_xlsx

def get_all_numbers(all_xlsx):
	all_numbers = []
	for xlsx in all_xlsx:
		for number in read_excel(xlsx,header=None).values.tolist():
			all_numbers += number
	unique_all_numbers = set(all_numbers)
	return unique_all_numbers

def write_sheet(all_numbers, sheet):
	if sheet[-5:] != ".xlsx":
		sheet = sheet+".xlsx"	
	workbook = xlsxwriter.Workbook(os.path.join("..", sheet))
	worksheet = workbook.add_worksheet()
	for row_number, phone_number in enumerate(all_numbers):        
		worksheet.write(row_number, 0, phone_number)
	workbook.close()

args = args.get_args_utils()

all_xlsx = join_all_xlsx(os.path.join("..","output"))
all_numbers = get_all_numbers(all_xlsx)
write_sheet(all_numbers, args.sheet)