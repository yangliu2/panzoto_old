#!/usr/bin/python

from user import User
import mysql
import util

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
	util.logo()
	response = raw_input("Please enter your name: ")

	first, last = get_name(response)

	user = User(first, last)

	return user

def process_response(user_response):
	
	user_response = user_response.lower()

	if user_response == 'exit':
		AI_response = 'See you!'
	else:
		AI_response = 'i cannot understand :('

	return AI_response

def question_loop(user):
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