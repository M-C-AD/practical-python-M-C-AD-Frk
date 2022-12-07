import csv

def portfolio_cost(filename):
	'''Computes the total cost (shares*price) of a portfolio file'''
	portfolio = []
	
	with open(filename) as f:
		rows = csv.reader(f)
		headers = next(rows)
		for row in rows:
			portfolio.append((row[0],int(row[1]),float(row[2])))
	return portfolio
