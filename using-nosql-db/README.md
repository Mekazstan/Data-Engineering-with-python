# -------- MONGODB --------
## Installing MONGODB
https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-ubuntu/
pip install pymongo

## Starting MONGODB
sudo systemctl start mongod
- Running in background
    sudo systemctl daemon-reload

## Checking status of MONGODB
sudo systemctl status mongod
- Enabling system reboot after start
    sudo systemctl enable mongod

## Stopping MONGODB
sudo systemctl stop mongod

## Re-starting MONGODB
sudo systemctl restart mongod

## Connecting to MONGODB
mongosh


NB: Data is stored as documents(records) while and collected as a collections(tables)
