import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://user2:PJS2021@cluster0.hin53.mongodb.net/test")
db = cluster["Testdaten"]
collection = db["customers"]


#zum Testen des Codes ID anpassen
#Robin: 1-10
#nico: 11-20
#Bene: 21-30
#Alpi: 31-40
post = {"_id":5, "name":"Robin", "score":1}

collection.insert_one(post)