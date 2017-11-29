
#ON MASTER BRANCH NEW SOMETHING! I DONT WANT THIS SHIT! 

import pymysql
import dbconfig

connection = pymysql.connect("localhost",
							  user=dbconfig.db_user,
							  password=dbconfig.db_password)

try:
	with connection.cursor() as cursor:
		sql = "CREATE DATABASE IF NOT EXISTS crimemap"
		cursor.execute(sql)
		sql = """CREATE TABLE IF NOT EXISTS crimemap.crimes (
			id int NOT NULL AUTO_INCREMENT,
			latitude FLOAT (10,6),
			longitude FLOAT(10,6),
			date DATETIME,
			category VARCHAR(50),
			description VARCHAR(1000),
			updated_at TIMESTAMP,
			PRIMARY KEY(id)
			)"""
		cursor.execute(sql)
		#comitting means now we are saving this
		connection.commit()
finally:
	connection.close()

#added this line , edited in master one
#added this second line after this one at up ^ in master branch