import yfinance as yf
import pandas as pd
import datetime
from numpy import nan
import math
import csv
import multiprocessing
from tqdm import tqdm


def get_list():
	uri1 = r'output/archive/all_tickers.json'
	reader = pd.read_json(uri1)
	tickers = [x for x in reader['symbol']]
	export = tickers
	return export


def cagr(start, end, div=nan):
	start = float(start)
	end = float(end)
	try:
		(int(div))
	except ValueError:
		div = 0
	return (((end + div) / start) ** (1 / 2)) - 1

def main():
	tickers = get_list()
	errors = []
	key_Errors = []
	series = []
	df = yf.download(tickers, start="2015-04-01", end="2017-05-01", interval='1mo')['Close']
	df = df.dropna(how='all')
	df = df.dropna(how="all", axis=1)
	# for ticker in tqdm(tickers):
	# 	try:
	# 		tick = yf.Ticker(ticker)
	# 		series.append(tick.info)
	# 	except ValueError:
	# 		errors.append(ticker)
	# 	except IndexError:
	# 		errors.append(ticker)
	# df = pd.DataFrame(series)
	# df.set_index(['symbol'])
	# dropa = ['companyOfficers', 'maxAge', 'website', 'longBusinessSummary', 'fax', 'trailingAnnualDividendYield',
	#          'navPrice', 'totalAssets', 'trailingAnnualDividendRate', 'expireDate', 'yield', 'algorithm',
	#          'dividendRate',
	#          'exDividendDate', 'circulatingSupply', 'startDate', 'lastMarket', 'maxSupply', 'openInterest',
	#          'volumeAllCurrencies', 'strikePrice', 'ytdReturn', 'fromCurrency', 'underlyingSymbol',
	#          'underlyingExchangeSymbol', 'headSymbol', 'messageBoardId', 'beta3Year', 'annualHoldingsTurnover',
	#          'morningStarRiskRating', 'revenueQuarterlyGrowth', 'fundInceptionDate', 'annualReportExpenseRatio',
	#          'fundFamily', 'lastDividendValue', 'threeYearAverageReturn', 'legalType', 'morningStarOverallRating',
	#          'lastCapGain', 'category', 'fiveYearAverageReturn', 'logo_url', 'address2', 'volume24Hr', 'toCurrency']
	# for d in dropa:
	# 	try:
	# 		df = df.drop(columns=d)
	# 		df.reindex(index=['symbol'])
	# 	except KeyError:
	# 		key_Errors.append(d)

	export = {}
	init = datetime.date(2015, 5, 1)
	fin = datetime.date(2017, 5, 1)
	for row in tqdm(df):
		start = 0
		end = 0
		dividend_sum = 0
		cagre = 0
		summ = 0
		beta = 0
		sector = ''
		name = ''
		currency = ''
		df2 = yf.Ticker(row).dividends
		try:
			tick = yf.Ticker(row).info
		except ValueError:
			errors.append(row)
			tick = {
				'currency': nan,
				'beta': nan,
				'shortName': nan,
				'sector': nan
			}
		except IndexError:
			errors.append(row)
			tick = {
				'currency': nan,
				'beta': nan,
				'shortName': nan,
				'sector': nan
			}
		for date in df2.index:
			if init <= date <= fin:
				summ += df2[date]
		try:
			sector = tick['sector']
		except KeyError:
			sector = nan
		start = df[row].dropna(how='any').head(1).values[0]
		end = df[row].dropna(how='any').tail(1).values[0]
		dividend_sum = summ
		cagre = (cagr(df[row].dropna(how='any').head(1), df[row].dropna(how='any').tail(1), summ))
		# print(tick)
		export[row] = {
			'name': tick['shortName'],
			'sector': sector,
			'beta(2020)': tick['beta'],
			'currency': tick['currency'],
			'first price': start,
			'last price': end,
			'dividends': dividend_sum,
			'CAGR': cagre,
		}
	export = pd.DataFrame(export)
	export = export.transpose()
	export.to_csv('output/CAGR.csv')
	#sector

	# df.to_csv('output/export_2.csv')
	# print(df)
	print(errors)
	print('Key Errors: {}'.format(key_Errors))


# with open('output/export.csv', 'w') as outfile:
# 	csv.writer(df, outfile)
# with open('output/errors.csv', 'w') as outfile:
# 	csv.writer(errors, outfile)


def it_to_csv():
	pass


if __name__ == '__main__':
	main()
