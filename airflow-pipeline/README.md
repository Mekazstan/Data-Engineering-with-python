# Building a CSV to a JSON data converter pipeline
The DAG in the code prints out a message using Bash, then reads the CSV and print a list of all the names.








# Installing Apache Airflow
sudo apt-get install software-properties-common
sudo apt-add-repository universe
sudo apt-get update
sudo apt-get install python-setuptools
sudo apt-get install python3-pip
python3 -m pip install --upgrade pip
sudo apt-get install libmysqlclient-dev
sudo apt-get install libssl-dev
sudo apt-get install libkrb5-dev

mkdir ~/airflow
export AIRFLOW_HOME=~/airflow
pip install apache-airflow
pip install typing_extensions

# Checking if installation worked
airflow version

# Intializing the database
airflow db init

# Create user
airflow users create --username admin --firstname Stan --lastname Adminstrator --role Admin --email mekastans@gmail.com
airflow users list

# Running in foreground
airflow webserver
airflow scheduler

# Running in background
airflow webserver -p 8081 --daemon
airflow scheduler --daemon

# Shut down scheduler & server running in background
kill $(cat ~/airflow/airflow-scheduler.pid)
kill $(cat ~/airflow/airflow-webserver.pid)

http://localhost:8081


# Applying changes made in config file
- Shutdown webserver & scheduler
- airflow db reset


# -------- MYSQL --------
## Installing MYSQL
sudo apt install mysql-server
## Checking & Starting MYSQL
sudo systemctl status mysql
sudo systemctl start mysql
## Stopping MYSQL
sudo service MYSQL stop

## Connecting to postgres
sudo mysql
sudo mysql -u root -p
## Setting Password
sudo mysql_secure_installation
ALTER USER 'root@localhost' IDENTIFIED WITH mysql_native_password BY 'root';

# Install MYSQL Workbench using snap
sudo snap install mysql-workbench-community

