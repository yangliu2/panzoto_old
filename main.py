#!/usr/bin/python

from user import User
import mysql
import util
from datetime import datetime

def get_name(string):
	'''get the first and last name'''

	split = string.split()

	if len(split) == 1:
		first = split[0]
		last = ''
	elif len(split) == 2:
		first = split[0]
		last = split[1]
	elif len(split) == 0:
		first = ''
		last = ''
	else:
		print 'error in name assigning'

	return first.title(), last.title()

def menu():

	# get the logo from util.py
	util.logo()

	# prompt for a name
	response = raw_input("Please enter your name: ")

	first, last = get_name(response)

	# get user info from user.py
	user = User(first, last)

	return user

def what(question):
	'''process questions start with 'what'. '''

	if 'what time is it' in question:
		return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def process_response(user_response):
	''' 
	the general processing function for the user response, will separate processing functions into difference categories 
	'''

	user_response = user_response.lower()

	if user_response == 'exit':
		AI_response = 'See you!'
	elif user_response.startswith('what'):
		AI_response = what(user_response)
	else:
		AI_response = 'i cannot understand :('

	return AI_response

def question_loop(user):
	''' question loop that will quit with 'exit' keyword'''

	user_response = ""
	while user_response != 'exit':
		user_response = raw_input("Panzoto > ")
		print process_response(user_response)

def main():
	'''main function'''
	user = menu()
	print "Greatings!", user.firstName, user.lastName
	question_loop(user)

if __name__ == '__main__':
	main()