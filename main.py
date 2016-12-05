#!/usr/bin/python

from user import User
# import mysql
from util import logo
from datetime import datetime
import random
from collections import namedtuple

NO_ANSWER = ['I cannot understand :(',
			 'Sorry, I have no idea what you said.',
			 'That is beyond me.',
			 "I'm too dumb to understand that."]

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
		print('error in name assigning')

	# define what's the returned field
	fullname = namedtuple('FullName', ['FirstName', 'LastName'])

	return fullname(first.title(), last.title())

def menu():

	# get the logo from util.py
	logo()

	# prompt for a name
	response = input("Please enter your name: ")

	first, last = get_name(response)

	# get user info from user.py
	user = User(first, last)

	return user

def what(question):
	'''process questions start with 'what'. '''

	if 'what time is it' in question:
		time = datetime.now()
		hour, minute = time.hour, time.minute
		return ["The time is "+time.strftime('%H:%M')+'.',
				"It's " + str(minute) + " past "+ str(hour) +" right now.",
				"It's "+time.strftime('%H:%M')+'.' ]
	else:
		return NO_ANSWER


def randomize_response(response):
	return random.choice(response)

def process_response(user_response):
	''' 
	the general processing function for the user response, will separate processing functions into difference categories 
	'''

	user_response = user_response.lower()

	if user_response == 'exit':
		AI_response = ['See you!', 'Bye!', 'Later!', 'Goodbye!', 'See you soon!']
		
	elif user_response.startswith('what'):
		AI_response = what(user_response)
		
	else:
		AI_response = NO_ANSWER

	# randomize answer to make it more like human
	AI_response = randomize_response(AI_response)

	return AI_response

def question_loop(user):
	''' question loop that will quit with 'exit' keyword'''

	user_response = ""
	while user_response != 'exit':
		user_response = input("Panzoto > ")
		print(process_response(user_response))

def main():
	'''main function'''
	user = menu()
	print("Greatings!"), user.firstName, user.lastName
	question_loop(user)

if __name__ == '__main__':
	main()