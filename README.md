# databases
##postgres
https://postgresql.r2schools.com/how-to-change-owner-of-database-in-postgresql/
https://www.cyberciti.biz/tips/postgres-allow-remote-access-tcp-connection.html
https://dba.stackexchange.com/questions/83984/connect-to-postgresql-server-fatal-no-pg-hba-conf-entry-for-host
https://tomcam.github.io/postgres/#opening-a-connection-locally

### Migrate sqlite3 to postgratesql data
https://www.dbsofts.com/articles/sqlite_to_postgresql/
sudo apt-get install libpq-dev python-dev
sudo apt-get install postgresql postgresql-contrib
pip install psycopg2==2.7.4

###otwieramy powloke
root@rd:~# su postgres

###logowanie do uzytkownika postgres
postgres@rd:/root$ psql -U postgres

###tworzymy uzytkownika "blog"
postgres@rd:/root$ createuser -dP blog

###logowanie do użytkownika blog
postgres@rd:/root$ psql -U blog -h localhost

postgres=# 

###zmiana wlasciciela bazy
postgres=# alter database blog owner to blog;

###Allow TCP/IP socket

root@rd:/etc/postgresql/11/main# vi /var/lib/pgsql/data/postgresql.conf
listen_addresses='*'
root@rd:/etc/postgresql/11/main# /etc/init.d/iptables restart

###next

root@rd:/etc/postgresql/11/main# vi /var/lib/pgsql/data/pg_hba.conf
host  all  all 0.0.0.0/0 md5
root@rd:/etc/postgresql/11/main# /etc/init.d/iptables restart


\l
\du
\q
\?
###łączymie sie z bazą
###sprwdzamy tabele
\c database
\dt
## mysql
mysql -p
MariaDB [(none)]> GRANT ALL PRIVILEGES ON *.* TO 'root'@'192.x.x.x' IDENTIFIED BY 'password';


## sqlite3
you need dll and file sqlite3.exe and sqlite3.

https://www.sqlite.org/download.html
only axtract all without install
or 
import sqlite3 from 

https://www.sqlite.org/cli.html