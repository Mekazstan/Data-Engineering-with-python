from pymongo import MongoClient
import json

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db_name = 'dataengineering'
db = client[db_name]

# Access the 'users' collection
collection = db['users']

# Retrieve all data from the 'users' collection
user_data = list(collection.find())

# Convert ObjectId to string for JSON serialization
for user in user_data:
    user['_id'] = str(user['_id'])

# Specify the JSON file path
json_file_path = 'users_data.json'

# Write the data to a JSON file
with open(json_file_path, 'w') as json_file:
    json.dump(user_data, json_file, indent=4)

print(f"Data from 'users' collection stored in {json_file_path}.")
