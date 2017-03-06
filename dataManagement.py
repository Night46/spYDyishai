# ##############################################################################
#
#	Imports
#
# ##############################################################################

import pymongo

# ##############################################################################
#
#	Main
#
# ##############################################################################


# class manageDB(spYDyisai, userInput):
# 	#TODO
# 	# convert all this class to use mongoDB
# 	# build the mongoDB file structure
# 	def findDB(self):
# 		if os.path.isfile(self.db_location+"/"+self.db_filename) == False:
# 			manageDB.createDB(self)
# 		elif os.path.isfile(self.db_location+"/"+self.db_filename) == True:
# 			pass
# 		else:
# 			print '''
# [!] There was a problem finding / creating the DB file.
# please scheck that the user running spYDyisai has appropriate permissions and start over'''
# 			quit()
#
# 	def createDB(self):
# 		db = sqlite3.connect(self.db_location+self.db_filename)
# 		db.close()
#
# 	def writeToDB(self):
# 		if os.path.isfile(self.resourcelist_location+"/"+self.resourcelist_filename) == True:
# 			print ''
# 			print '[-] Checking if resource already exists in the DB.'
# 			conf = SafeConfigParser()
# 			conf.read(self.resourcelist_location+"/"+self.resourcelist_filename)
# 			for section_name in conf.sections():
# 				resource_URL = conf.get(section_name, 'resource')
# 				resource_user = conf.get(section_name, 'username')
# 				resource_pass = conf.get(section_name, 'password')
# 				db = sqlite3.connect('resourceDB')
# 				cursor = db.cursor()
# 				cursor.execute('SELECT * FROM sqlite_master WHERE type="table"')
# 				tables_list = cursor.fetchall()
# 				tables_exsist = resource_URL in chain.from_iterable(tables_list)
#
# 				if tables_exsist != True:
# 					cursor.execute('CREATE TABLE IF NOT EXISTS \"'+resource_URL+'\" (url text, credentials text, username text, password text, filename text, filetype text, status text)')
# 					print '[-] Added recource '+resource_URL+' to DB.'
# 					cursor.execute('INSERT INTO \"'+resource_URL+'\" VALUES (\"'+resource_URL+'\", "credentials", \"'+resource_user+'\", \"'+resource_pass+'\", "filename", "filetype", "status" )')
# 					print '[-] Added recource credentials to table.'
# 					db.commit()
# 				elif tables_exsist == True:
# 					print ''
# 					print '[!] Recource '+resource_URL+' already exsits in DB.'
# 					print '[-] Checking if any update is requiered.'
# 				db.close()
#
#
# 		elif os.path.isfile(userFilePath+"/"+self.resourcelist_filename) == True:
# 			print ''
# 			print '[-] Checking if resource already exists in the DB.'
# 			conf = SafeConfigParser()
# 			conf.read(self.resourcelist_location+"/"+self.resourcelist_filename)
# 			for section_name in conf.sections():
# 				resource_URL = conf.get(section_name, 'resource')
# 				resource_user = conf.get(section_name, 'username')
# 				resource_pass = conf.get(section_name, 'password')
# 				db = sqlite3.connect('resourceDB')
# 				cursor = db.cursor()
# 				cursor.execute('SELECT * FROM sqlite_master WHERE type="table"')
# 				tables_list = cursor.fetchall()
# 				tables_exsist = resource_URL in chain.from_iterable(tables_list)
#
# 				if tables_exsist != True:
# 					cursor.execute('CREATE TABLE IF NOT EXISTS \"'+resource_URL+'\" (url text, credentials text, username text, password text, filename text, filetype text, status text)')
# 					print '[-] Added recource '+resource_URL+' to DB.'
# 					cursor.execute('INSERT INTO \"'+resource_URL+'\" VALUES (\"'+resource_URL+'\", "credentials", \"'+resource_user+'\", \"'+resource_pass+'\", "filename", "filetype", "status" )')
# 					print '[-] Added recource credentials to table.'
# 					db.commit()
# 				elif tables_exsist == True:
# 					print ''
# 					print '[!] Recource '+resource_URL+' already exsits in DB.'
# 				db.close()
#
# 	def readTablesFromDB(self):
# 		db = sqlite3.connect('resourceDB')
# 		db.row_factory = sqlite3.Row
# 		cursor = db.cursor()
# 		cursor.execute('SELECT name FROM sqlite_master WHERE type="table"')
# 		for table_row in cursor.fetchall():
# 			table = table_row[0]
# 			print '	[-] '+table
# 			print ''
# 		db.close()
#
# 	def readTablesDataFromDB(self):
# 		db = sqlite3.connect('resourceDB')
# 		db.row_factory = sqlite3.Row
# 		cursor = db.cursor()
# 		cursor.execute('SELECT name FROM sqlite_master WHERE type="table"')
# 		for table_row in cursor.fetchall():
# 			table = table_row[0]
# 			print '	[-] '+table
# 			print ''
# 			db_data = cursor.execute('SELECT url, credentials, username, password, filename, filetype, status FROM \"'+table+'\"')
# 			for row in db_data:
# 			   print 'URL 			= ', row[0]
# 			   print 'CREDENTIALS 		= ', row[1]
# 			   print 'USERNAME 		= ', row[2]
# 			   print 'PASSWORD 		= ', row[3]
# 			   print 'FILENAME 		= ', row[4]
# 			   print 'FILETYPE 		= ', row[5]
# 			   print 'STATUS 			= ', row[6]
# 			   print ''
# 		db.close()
#
# 	def readSingleTableData(self):
# 		db = sqlite3.connect('resourceDB')
# 		db.row_factory = sqlite3.Row
# 		cursor = db.cursor()
# 		cursor.execute('SELECT name FROM sqlite_master WHERE type="table"')
# 		chosen_table = cursor.fetchall()
# 		self.user_table_selection = raw_input().lower
# 		try:
# 			print ' [-] '+self.user_table_selection()
# 			print ''
# 			db_data = cursor.execute('SELECT url, credentials, username, password, filename, filetype, status FROM \"'+self.user_table_selection()+'\"')
# 			for row in db_data:
# 			   print 'URL 			= ', row[0]
# 			   print 'CREDENTIALS 		= ', row[1]
# 			   print 'USERNAME 		= ', row[2]
# 			   print 'PASSWORD 		= ', row[3]
# 			   print 'FILENAME 		= ', row[4]
# 			   print 'FILETYPE 		= ', row[5]
# 			   print 'STATUS 			= ', row[6]
# 			   print ''
# 		except:
# 			print '[!] Could not find the requested table'
# 			print ''
# 			db.close()
# 			userInteraction.guided_wellcome_options(self)
#
# 	def editTableData(self):
# 		dataField = raw_input().lower
#
# 		while dataField() not in ['', 'no', 'none', 'ur', 'url', 'us', 'username', 'pa', 'password']:
# 			print '[!] Please choos only "none", "url", "username", "password" or leave blank for default'
# 			dataField = raw_input().lower
# 		if dataField() in ['ur', 'url']:
# 			print '[-] please type in the new URL value'
# 			new_url = raw_input().lower
# 			db = sqlite3.connect('resourceDB')
# 			cursor = db.cursor()
# 			cursor.execute('UPDATE \"'+self.user_table_selection()+'\" SET url=?',(new_url(),))
# 			db.commit()
# 			db.close()
# 		elif dataField() in ['us', 'username']:
# 			print '[-] Please type in the new USERNAME value'
# 			new_username = raw_input()
# 			db = sqlite3.connect('resourceDB')
# 			cursor = db.cursor()
# 			cursor.execute('UPDATE \"'+self.user_table_selection()+'\" SET username=?',(new_username,))
# 			db.commit()
# 			db.close()
# 		elif dataField() in ['pa', 'password']:
# 			print '[-] Please type in the new PASSWORD value'
# 			new_password = getpass.getpass()
# 			db = sqlite3.connect('resourceDB')
# 			cursor = db.cursor()
# 			cursor.execute('UPDATE \"'+self.user_table_selection()+'\" SET password=?',(new_password,))
# 			db.commit()
# 			db.close()
# 		elif dataField() in ['', 'no', 'none']:
# 			print 'you chose to no edit anything, mooving on..'
# 		else:
# 			print 'You broke me :/'
# 			quit()
#
# 	def deleteResourceFromDB(self):
# 		delete_table = raw_input().lower
#
# 		while delete_table() == '':
# 			print '[!] Table name can\'t be left blank'
# 			print ''
# 			print '[-] Please select which table you would like to delete'
# 			delete_table = raw_input().lower
#
# 		db = sqlite3.connect('resourceDB')
# 		cursor = db.cursor()
# 		cursor.execute('SELECT * FROM sqlite_master WHERE type="table"')
# 		tables_list = cursor.fetchall()
# 		tables_exsist = delete_table() in chain.from_iterable(tables_list)
#
# 		if tables_exsist == True:
# 			cursor.execute('DROP TABLE IF EXISTS \"'+delete_table()+'\"')
# 			db.commit()
# 			print '[!] Done, check status with DB full data view'
# 		elif tables_exsist != True:
# 			print '[!] Could not find the table in the DB'
#
# 		db.close()



if __name__ == '__main__':
	pass
