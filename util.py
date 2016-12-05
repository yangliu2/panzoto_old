#!/usr/bin/python
from functools import wraps
from contextlib import contextmanager

def logo():
	print ('     _____    __       _        ____     ___    _______   ___   ')
	print ('    /    /   /  |     / |    /     /    /   \      /     /   \  ') 
	print ('   /____/   /___|    /  |   /     /    /     \    /     /     \ ')
	print ('  /        /    |   /   |  /     /     \     /   /      \     / ')
	print (' /        /     |  /    |_/     /____   \___/   /        \___/  ') 
	print ('----------------------------------------------------------------')

def cache(func):
	'''
	decorator to cache the url link
	'''

	saved= {}
	@wraps(func)
	def newfunc(*args):
		if args in saved:
			return newfunc(*args)
		result = func(*args)
		saved[args] = result
		return result
	return newfunc

@contextmanager
def ignored(*exceptions):
	'''ignore exceptions'''

	try:
		yield
	except exceptions:
		pass

@cache
def web_lookup(url):
	return urllib.urlopen(url).read()

def main():
	url = 'http://www.panzoto.com'
	web_lookup()

if __name__ == '__main__':
	main()