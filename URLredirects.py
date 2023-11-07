import requests
from openpyxl import load_workbook

file = input("Enter Path of the Excel File (including file extention): ")

workbook = load_workbook(file)

sheet = workbook.active


for x in range(sheet.max_row - 1):
	toBeRedirectedURL = (sheet.cell(row = x + 2, column = 1).value)


	r = requests.get(toBeRedirectedURL)
	redirectedURL = r.url
	strippedURL = redirectedURL.split("?", 1)[0]

	cell = str("B" + str(x + 2))
	sheet[cell] = strippedURL
	print(strippedURL)

workbook.save(file)
print("FINISHED")
