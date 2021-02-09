import pymongo
import json


def get_data_entities(data):
    newdata = json.loads(data)
    mongo = pymongo.MongoClient("mongodb://localhost:27017")
    mydb = mongo["datacrawling"]
    collection = mydb["crawling"]
    query = {"url":newdata["url"]}
    D = []
    for x in collection.find(query):
        D = x
    print(D)
    return D["data"]
