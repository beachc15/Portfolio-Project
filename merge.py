import pandas as pd

file1 = 'output/export.csv'
file2 = 'output/export2.csv'

df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

print(df1.columns)
print(df2.columns)

dropa = ['Unnamed: 0', 'companyOfficers', 'maxAge', 'website', 'longBusinessSummary', 'fax', 'trailingAnnualDividendYield',
	         'navPrice', 'totalAssets', 'trailingAnnualDividendRate', 'expireDate', 'yield', 'algorithm',
	         'dividendRate',
	         'exDividendDate', 'circulatingSupply', 'startDate', 'lastMarket', 'maxSupply', 'openInterest',
	         'volumeAllCurrencies', 'strikePrice', 'ytdReturn', 'fromCurrency', 'underlyingSymbol',
	         'underlyingExchangeSymbol', 'headSymbol', 'messageBoardId', 'beta3Year', 'annualHoldingsTurnover',
	         'morningStarRiskRating', 'revenueQuarterlyGrowth', 'fundInceptionDate', 'annualReportExpenseRatio',
	         'fundFamily', 'lastDividendValue', 'threeYearAverageReturn', 'legalType', 'morningStarOverallRating',
	         'lastCapGain', 'category', 'fiveYearAverageReturn', 'logo_url', 'address2', 'volume24Hr', 'toCurrency']
key_Errors = []
li = [df1, df2]
for l in li:
	for d in dropa:
		try:
			df = l.drop(columns=d)
			df.reindex(index=['symbol'])
		except KeyError:
			key_Errors.append(d)
print(key_Errors)
df1.to_csv('export_1.csv')
df2.to_csv('export_2.csv')