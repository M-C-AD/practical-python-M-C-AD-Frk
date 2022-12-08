import csv

def read_portfolio(filename):
	'''Computes the total cost (shares*price) of a portfolio file'''
	portfolio = []
	
	with open(filename) as f:
		rows = csv.reader(f)
		headers = next(rows)
		for row in rows:
			stock = {'name':row[0], 'shares':int(row[1]), 'price':float(row[2])}
			portfolio.append(stock)
	return portfolio
