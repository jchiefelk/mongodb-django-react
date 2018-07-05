from __future__ import unicode_literals
import json
from bson import json_util
# from pymongo import MongoClient
# client = MongoClient('127.0.0.1', 27017)
# db = client.test

class CreateCache:

	def __init__(self):
		self.cursor = self.setCursor()
		self.data = self.setList()

	def setCursor(self):
		cursor = db['tomis'].find({})
		return cursor

	def setList(self):
		doclist=[]
		for doc in self.cursor:
			doclist.append(doc)

		return doclist

from django.db import models

# Create your models here.

class Data(models.Model):

	data = models.TextField()
	# data = CreateCache().data