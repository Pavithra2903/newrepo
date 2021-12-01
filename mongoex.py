from pymongo import MongoClient
#To establish connection
client = MongoClient('localhost', 27017)
#To create DB
mydb=client['student']
#To print the list of DB
print(client.list_database_names())
#To create a collection
mycol = mydb['studentdet']
#To print the list of collections
print(mydb.list_collection_names())

#Insert values into the collection studentdet
data = { "Roll_No": "101", "name": "John", "dept": "CSE" }

x = mycol.insert_one(data)

print("Rows after single insert:")
#To retrieve a single record
x = mycol.find_one()

print(x)

#To check whether the DB is available
dblist = client.list_database_names()
if 'student' in dblist:
  print("The database exists.")

#To check whether the collection EXISTS
collist = mydb.list_collection_names()
if 'customers' in collist:
  print("The collection exists.")

#To insert multiple rows
mylist = [
  { "Roll_No": "102", "name": "Kumar", "dept": "CSE"},
  { "Roll_No": "103", "name": "Mani", "dept": "IT"},
  { "Roll_No": "104", "name": "Peter", "dept": "MECH"},
  { "Roll_No": "105", "name": "Catherine", "dept": "ECE"},
  { "Roll_No": "106", "name": "Sanjay", "dept": "EEE"},
]

x = mycol.insert_many(mylist)

print("Rows after Multiple Insert:")
#To retrieve Multiple records
for x in mycol.find():
  print(x)

#To update a row in the collection
x=mycol.update_one({"name":"John"},{"$set" : {"dept": "IT"}})

print("Rows after update:")
for x in mycol.find():
  print(x)

#TO delete a row from the collection
x=mycol.delete_one({"name":"Catherine"})

print("Rows after Delete:")
for x in mycol.find():
#print the result
  print(x)