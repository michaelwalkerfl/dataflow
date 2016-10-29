#!/usr/bin/python
import pymysql
from sys import argv
from pync import Notifier

'''
Create your MySQL table with this command:

CREATE TABLE `Email` (
`email_id` INT(10) UNSIGNED NOT NULL AUTO_INCREMENT,
`email` VARCHAR(58) NOT NULL,
`is_opted_out` tinyint(1) UNSIGNED NOT NULL DEFAULT 0,
`has_bounced` tinyint(1) UNSIGNED NOT NULL DEFAULT 0,
PRIMARY KEY (`email_id`),
UNIQUE (`email`)
) ENGINE=InnoDB CHARSET=utf8 COLLATE utf8_unicode_ci;

'''

# Establish connection to local MySQL database
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='yourpasswordhere', db='yourdatabasehere')

cursor = db.cursor()

s = str(file('%s' % argv[1]).read())
w = s.split('\n')

success = 0
failed = 0

for e in w:
	try:
		cursor.execute("INSERT INTO email(email) VALUES(%s)", (e))
		db.commit()
		success += 1
		print e + " was successfully added to database."
	except:
		db.rollback()
		failed += 1
		print e + " has failed to be added to database."


db.close()
Notifier.notify('Your import is complete.', title='Python email list importer')
print 'There were %s emails successfully added to the database.' % success
print 'There were %s emails that failed to be added to the database.' % failed
