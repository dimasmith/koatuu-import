from pymongo import MongoClient


def write_raions(raions, collection='raions', database='cities', mongo_uri='mongodb://localhost:27017/'):
    client = MongoClient(mongo_uri)
    db = client[database]
    collection = db[collection]
    collection.insert_many(raions)