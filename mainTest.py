__author__ = "Gryph"
import pymongo
import random
from pymongo import MongoClient
from random import randint
uri = "mongodb://127.0.0.1:27017"
client = pymongo.MongoClient(uri)
database = client['movieCard']
collection = database['movieCardList']

cards = collection.find({})
deck = []
#dbLen = cards.count()
dLen = 0
ranCard = randint(1,4)
#while dLen <= dbLen:
#    deck.append(collection.find([dbLen]))
#    dLen += 1

 #   dLen += 1
for card in cards:
	print(card)
print(deck)
#print(dbLen)
print(ranCard)