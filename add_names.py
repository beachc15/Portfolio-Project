import csv
import tqdm
import requests
import lxml.html


def main():
	get_names()


def get_names():
	urls = ['https://www.investing.com/indices/japan-ni225-components',
	        'https://www.investing.com/indices/nasdaq-composite-components',
	        'https://www.investing.com/indices/germany-30-components',
	        'https://www.investing.com/indices/france-40-components',
	        'https://www.investing.com/indices/eu-stoxx50-components',
	        'https://www.investing.com/indices/netherlands-25-components',
	        'https://www.investing.com/indices/spain-35-components',
	        'https://www.investing.com/indices/switzerland-20-components',
	        'https://www.investing.com/indices/psi-20-components',
	        'https://www.investing.com/indices/bel-20-components',
	        'https://www.investing.com/indices/omx-stockholm-30-components',
	        'https://www.investing.com/indices/omx-copenhagen-25-components',
	        'https://www.investing.com/indices/mcx-components',
	        'https://www.investing.com/indices/rtsi-components',
	        'https://www.investing.com/indices/shanghai-composite-components',
	        'https://www.investing.com/indices/szse-component-components',
	        'https://www.investing.com/indices/hang-sen-40-components',
	        ]
	for url in urls:
		print(url)
		page = requests.get(url, stream=True)
		page.raw.decode_content = True
		tree = lxml.html.parse(page.raw)
		print(page.content)


if __name__ == '__main__':
	main()
