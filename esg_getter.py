import yfinance as yf
import pandas as pd
import math
import json
import multiprocessing
from tqdm import tqdm


def get_list():
	uri1 = r'output/all_tickers.json'
	reader = pd.read_json(uri1)
	tickers = [x for x in reader['symbol']]
	export = tickers
	print(export)
	return export


def split_symbols(tickers, coreno, corecount):
	coreno -= 1
	cores = len(tickers) / corecount
	return tickers[coreno * math.ceil(cores): (coreno + 1) * math.ceil(cores)]


def main(number):
	tickers = get_list()
	symbols = split_symbols(tickers, number, multiprocessing.cpu_count() * 2)
	errors = []
	series = {}
	for symbol in tqdm(symbols):
		try:
			tick = yf.Ticker(symbol)
			if tick.sustainability is None:
				pass
			else:
				tick = tick.sustainability.transpose()
				if int(tick['percentile']) < 40:
					series[symbol] = tick.to_json()
		except:
			errors.append(symbol)
	with open('export_{}.json'.format(number), 'w') as outfile:
		json.dump(series, outfile)
	with open('errors_{}.json'.format(number), 'w') as outfile:
		json.dump(errors, outfile)


# return number, symbols


if __name__ == '__main__':
	cores = multiprocessing.cpu_count() * 2
	p = multiprocessing.Pool(cores)
	print((p.map(main, [1, 2, 3, 4, 5, 6, 7, 8])))
