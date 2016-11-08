import MySQLdb
import peewee
from peewee import *

db = MySQLDatabase('Panzoto', user='root',passwd='Demo3456')
'''
class Book(peewee.Model):
    author = peewee.CharField()
    title = peewee.TextField()

    class Meta:
        database = db

Book.create_table()
book = Book(author="me", title='Peewee is cool')
book.save()
for book in Book.filter(author="me"):
    print book.title
'''