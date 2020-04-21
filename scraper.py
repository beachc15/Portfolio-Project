import lxml.html
import requests
from tqdm import tqdm
import json
import csv

base_url = 'https://finance.yahoo.com/lookup?s='
ex_dest = '/output/'
ex = []


def get_names():
	from os import listdir
	from os.path import isfile, join
	tickers_ex = []
	mypath = 'input/'
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
	for file in onlyfiles:
		with open('input/{}'.format(file), newline='') as csvfile:
			reader = csv.reader(csvfile, delimiter=',', quotechar='|')
			for row in reader:
				tickers_ex.append(row[0])
	return tickers_ex


def meat(names):
	error = []
	for name in tqdm(names):
		print(name)
		page = requests.get('{}{}'.format(base_url, name), stream=True)
		page.raw.decode_content = True
		tree = lxml.html.parse(page.raw)
		xpaths = '//*[@id="lookup-page"]/section/div/div/div/div/table/tbody/tr[1]/td[1]/a'
		x = tree.xpath(xpaths)
		out1 = {
			'name': name,
			'symbol': x[0].text,
			'index': 'index'
		}
		ex.append(out1)

	with open('output/archive/all_tickers.json', 'w') as outfile:
		json.dump(ex, outfile, indent=4)
	with open('output/archive/errors.json', 'w') as outfile2:
		json.dump(error, outfile2, indent=4)
	return 'done'


def main():
	tickers = get_names()
	# get names
	return meat(tickers)


if __name__ == '__main__':
	print(main())
