from pymongo import MongoClient, GEOSPHERE


def insert_raions(raions, collection_name='raions', database_name='cities', mongo_uri='mongodb://localhost:27017/'):
    client = MongoClient(mongo_uri)
    db = client[database_name]
    collection = db[collection_name]
    collection.drop()
    collection.insert_many(raions)
    collection.create_index([('loc', GEOSPHERE)])
