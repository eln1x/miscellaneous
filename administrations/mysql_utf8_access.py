#!/usr/bin/env python
#MYSQL CREATE UTF8 DATABASE WITH ACCESS USERNAME & PASSWORD
#Ahmed Mahfouz AKA _N1X_
import sys,os

mysql_root="root"
mysql_pwd="mysqlrootpassword_here"
hostname="localhost"
try:
	db = sys.argv[1]
	username = sys.argv[2]
	password = sys.argv[3]


	create_db = "CREATE DATABASE " + "`"+ db + "`" + " CHARACTER SET utf8 COLLATE utf8_general_ci;"
	adddb_user =  "GRANT ALL ON `" + db  + "`.* TO '" + username+ "'@'localhost' IDENTIFIED BY " +"'"+ password + "';"
	reload = "FLUSH PRIVILEGES;"
	show_query = raw_input("Do u want to show mysql query Y/N (default N)")
	if show_query.lower() == 'y':
		print create_db
		print adddb_user
		print reload
	update_db = raw_input("if you want to apply  prees Y/N: ")
	if update_db.lower() == 'y':
		sql_create = "echo %s|mysql -u %s -p%s -h%s" %(create_db.strip(";").replace("`","\`"),mysql_root,mysql_pwd,hostname)
		sql_adduser = "echo %s|mysql -u %s -p%s -h%s" %(adddb_user.strip(";").replace("`","\`").replace("'","\\'"),mysql_root,mysql_pwd,hostname)
		sql_commit ="echo %s|mysql -u %s -p%s -h%s" %(reload.strip(";"),mysql_root,mysql_pwd,hostname)
		#print sql_create
		#print "x"*10
		#print adddb_user
		#print sql_adduser
		print "Creating Database"
		os.system(sql_create)
		print "Adding User to Database"
		os.system(sql_adduser)
		print "Finishing"
		os.system(sql_commit)

except IndexError:
	print "usage: python mysql_db_user_pass_gen.py database_name username password"
	exit()
