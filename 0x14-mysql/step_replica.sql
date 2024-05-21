#!/usr/bin/bash
#Steps to establish replication process between servers
replica_server_ip=54.234.60.29
source_server_ip=54.162.75.67
sudo ufw allow from $replica_server_ip to any port 3306
sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf
bind-address = $source_server_ip
#uncomment server-id = 1
#uncomment log_bin = /var/log/mysql/mysql-bin.log
