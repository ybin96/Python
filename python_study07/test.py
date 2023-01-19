import pymongo
url = 'mongodb://127.0.0.1:27017';
dbName = 'mydb';


client = pymongo.MongoClient(url)
db = client[dbName]
print(db.my_collection)
# print(db.my_collection.insert_one({"x": 10}).inserted_id)
# db.my_collection.insert_one({"x": 8})
# db.my_collection.insert_one({"x": 11})
print(db.my_collection.find_one())

list = db.my_collection.find()
for row in list:
    print(row)

# for item in db.my_collection.find().sort("x", pymongo.ASCENDING):
# ...     print(item["x"])
