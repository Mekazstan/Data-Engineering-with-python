from faker import Faker
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['dataengineering']
collection = db['users']

# Fake()r instance
fake = Faker

# Loop 1000 times to generate and insert data
for _ in range(1000):
    user_data = {
        'name': fake.name(),
        'street': fake.street_address(),
        'city': fake.city(),
        'zip': fake.zipcode(),
    }

    # Insert data into MongoDB collection
    collection.insert_one(user_data)

print("Data inserted into MongoDB.")
