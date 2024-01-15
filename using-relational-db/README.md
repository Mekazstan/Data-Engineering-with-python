# -------- MYSQL --------
## Installing MYSQL
sudo apt install mysql-server
## Checking & Starting MYSQL
sudo systemctl status mysql or systemctl is-active mysql
sudo systemctl start mysql
## Stopping MYSQL
sudo service MYSQL stop

## Connecting to postgres
sudo mysql
sudo mysql -u root -p
## Setting Password
sudo mysql_secure_installation
ALTER USER 'root@localhost' IDENTIFIED WITH mysql_native_password BY '********';

# Install MYSQL Workbench using snap
sudo snap install mysql-workbench-community

