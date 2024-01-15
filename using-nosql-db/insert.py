from faker import Faker
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db_name = 'dataengineering'
db = client[db_name]

# Check if the database exists, create it if not
if db_name not in client.list_database_names():
    print(f"Creating MongoDB database: {db_name}")
    db = client[db_name]
    
collection = db['users']

# Fake()r instance
fake = Faker()

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
