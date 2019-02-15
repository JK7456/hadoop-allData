#!/bin/bash
# This script is used to automatic  install mysql-server ,create database and tables
# This mysql-server for paas AI Platform,otherwise please modify the 21-24num  
# USAGE: ./mysql.sh  password    "The password is you mysql-server's password"
#
apt update
chmod a+x $PWD/*.sh
./expect.sh root                                                                                                                                                            ./etc/init.d/mysql restart
mysql -uroot -proot -e "
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'root' WITH GRANT OPTION;
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
#/etc/init.d/mysql restart

