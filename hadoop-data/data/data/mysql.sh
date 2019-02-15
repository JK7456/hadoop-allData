#!/bin/bash
# This script is used to automatic  install mysql-server ,create database and tables
# This mysql-server for paas AI Platform,otherwise please modify the 21-24num  
# USAGE: ./mysql.sh  password    "The password is you mysql-server's password"
#
apt update
apt  install expect -y
chmod a+x $PWD/*.sh
mysql -V
if [ $? -eq 0 ];then
	echo "mysql-server already exists"
else
# Install mysql-server
	./expect.sh $1
	echo "***********mysql-server install success**********"
	/etc/init.d/mysql start
fi
#Allow remote machices access and create database and tables
sed -i 's/127.0.0.1/0.0.0.0/g'  /etc/mysql/mysql.conf.d/mysqld.cnf
mysql -uroot -p$1 -e "
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY '$1' WITH GRANT OPTION;
FLUSH PRIVILEGES;
drop database if exists job;
create database job;
use job;
source $PWD/job.sql;

drop database if exists movie;
create database movie;
use movie;
source $PWD/movie.sql;

quit"
echo "********tables insect into mysql*************"
/etc/init.d/mysql restart

