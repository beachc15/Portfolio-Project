import pandas as pd
import json
import yfinance as yf
from tqdm import tqdm

l = [1, 2, 3, 4, 5, 6, 7, 8]
tickers = []
for x in l:
	with open('export_{}.json'.format(x), 'r') as infile:
		reader = (json.load(infile))
	for z in reader:
		tickers.append(z)

cap = {}
for x in tqdm(tickers):
	tick = yf.Ticker(x).info
	cap[tick['longName']] = (tick['marketCap'])
	# for y in tick:
	# 	print(y)
print(cap)