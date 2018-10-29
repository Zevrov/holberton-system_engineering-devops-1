# 0x03-more_functions_nested_loops

<img alt="DevOps" src=https://github.com/yook00627/holberton-system_engineering-devops/blob/master/0x14-mysql/KkrkDHT.png>

**What you should learn from this project**

    At the end of this project you are expected to be able to explain to anyone, without the help of Google:

* What is the main role of a database
* What is a database replica
* What is the purpose of a database replica
* Why database backups need to be stored in different physical locations
* What operation should you regularly perform to make sure that your database backup strategy actually works

## Exercises

[0-mysql_configuration_primary](./0-mysql_configuration_primary)
[0-mysql_configuration_replica](./0-mysql_configuration_replica)
```
Install and configure MySQL onweb-01 and web-02 so that they for a primary/replica (master/slave) cluster.
Having a replica member on for your MySQL database has 2 advantages:
```
* Redundancy: if you lose one of the database servers, you will still have another working one and a copy of your data
* Load distribution: you can split the read operations between the 2 servers, allowing to reduce the load on the primary member and improve query response speed
* MySQL primary must be hosted on web-01 - do no use the bind-address, just comment this parameter
* MySQL replica must be hosted on web-02
* Setup replication for the MySQL database named holberton
* Provide your MySQL primary configuration as answer file(my.cnf) with the name 0-mysql_configuration_primary
* Provide your MySQL replica configuration as answer file with the name 0-mysql_configuration_replica
* Create a MySQL user named holberton, password projectcorrection280hbtn with read access on replication status (the checker will use it to verify that replication is running fine)
* Make sure that task #3 of your SSH project is completed for web-01 and web-02, the checker will connect to your servers to check MySQL status - mainly this task: Let me in! 
* Make sure to do task #3 of your SSH project for the web-02 server as the key needs to be on both servers
* Make sure you have at least one table with one row in your primary database before starting the replication
* Once MySQL is installed on web-01, create a database containing at least one table with one record (name and what type of fields does not matter)
* Once MySQL replication is setup, add a new record in your table via MySQL on web-01 and check if the record has been replicated in MySQL web-02. If you see it, it means your replication is working!

[1-mysql_backup](./1-mysql_backup)
```
What if the data center where both your primary and replica database servers are hosted are down because of a power outage or even worse: flooding, fire? Then all your data would inaccessible or lost. That’s why you want to backup and store them in a different system in another physical location. This can be achieved by dumping your MySQL data, compressing them and storing them in a different data center.
Write a Bash script that generates a MySQL dump and creates a compressed archive out of it.
Requirements:
```
* The MySQL dump must contain all your MySQL databases
* The MySQL dump must be named backup.sql
* The MySQL dump file has to be compressed to a tar.gz archive
* This archive must have the following name format: day-month-year.tar.gz
* The user to connect to the MySQL database must be root
* The Bash script accepts one argument that is the password used to connect to the MySQL database

## Author
### Kevin Yook 
Email: <yook00627@gmail.com> Twitter: [@yook00627](https://twitter.com/yook00627)
