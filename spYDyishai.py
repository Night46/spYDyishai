#!/usr/bin/env python

#TODO
# add text colors and decorations

# ##############################################################################
#
#	Prerequisites
#
# ##############################################################################

#

# ##############################################################################
#
#	Imports
#
# ##############################################################################

import gmailConnect
import dataManagement
import sys
import os
import argparse
import getpass
import pymongo
from itertools import chain
from ConfigParser import SafeConfigParser


# ##############################################################################
#
#	Main
#
# ##############################################################################

class spYDyishai():
	def __init__(self):
		self.credentialslist_location = os.getcwd()
		self.credentialslist_filename = 'credentialslist.ini'

		self.db_location = os.getcwd()
		self.db_filename = 'resourceDB'

		self.credentialslist_dictionary = {}

		self.stdout_orig = sys.stdout


class userInput(spYDyishai):
	def Credentials_Resorce(self):
		print '''
Please provide a set of username and password that are valid for Gmail login
[!] user format >	username@domain.com

'''
		print '[-] Please type your username for the resource: '
		resource_user = raw_input()
		print '[-] Please type your password for the resource: '
		resource_pass = getpass.getpass()
		print '[-] Please retype your password for the resource:'
		resource_passRT = getpass.getpass()

		while resource_pass != resource_passRT:
			print ''
			print '[!] the passwords didn\'t match'
			print '[-] Please type your password for the resource: '
			resource_pass = getpass.getpass()
			print '[-] Please retype your password for the resource:'
			resource_passRT = getpass.getpass()
		else:
			pass

		print 'Is the spelling correct for: ' +resource_user+ 'with password: '+resource_pass+' (Y/n)'
		resourceYN = raw_input().lower

		while resourceYN() not in ['y', 'Y', 'n', 'N', '']:
			print '[!] Please choose only "y", "n" or leave blank for default'
			resourceYN = raw_input().lower
		if resourceYN() in ['y','Y', '']:
			pass
		elif resourceYN() == 'n':
			userInput.Credentials_Resorce(self)
		else:
			print 'You broke me :/'
			quit()

		self.credentialslist_dictionary.update({"username":username, "password":password})

		for i in str(resource_number):
			n = resource_number
			f = open(self.credentialslist_location+"/"+self.credentialslist_filename, 'a')
			sys.stdout = f
			print '[resource'+str(n)+']'
			n = n+1
			for i in self.credentialslist_dictionary.keys():
				print i +' = '+ self.credentialslist_dictionary[i]
			print ''
			sys.stdout = self.stdout_orig
			f.close()


	def Uresourcefile(self):
		print '[-] Please provide a full path for the credentialslist.ini file:'
		Ucredentialslist_location = raw_input()
		global userFilePath
		userFilePath = Ucredentialslist_location
		if os.path.isfile(Ucredentialslist_location+"/"+self.credentialslist_filename) == True:
			userInteraction.credentialslist_read(self)
		else:
			userInteraction.credentialslist_find(self)


class userInteraction(spYDyishai, userInput):
	def wellcome(self):
		parser = argparse.ArgumentParser()
		parser.add_argument('--sh', help='print out a short help', action='store_true', default=False)
		parser.add_argument('--fh', help='print out the full extended help file', action='store_true', default=False)
		parser.add_argument('--p', help='set the current session proxy settings', action='store_true', default=False)
		parser.add_argument('--mi', help='manual input for new credentials and run', action='store_true', default=False)
		parser.add_argument('--fi', help='read new credentials from file and run', action='store_true', default=False)
		parser.add_argument('--dbi', help='run again from resource in th DB', action='store_true', default=False)
		parser.add_argument('--os', help='print the crwaler results only to screen', action='store_true', default=False)
		parser.add_argument('--of', help='write the crawler results to a file', action='store_true', default=False)
		parser.add_argument('--odb', help='write the crawler results to the DB', action='store_true', default=False)
		parser.add_argument('--rfdb', help='read results from the DB', action='store_true', default=False)
		parser.add_argument('--dfdb', help='delete results from the DB', action='store_true', default=False)
		parser.add_argument('--dadb', help='delete all the resources from the DB', action='store_true', default=False)
		parser.add_argument('--rff', help='read results from an output file', action='store_true', default=False)
		parser.add_argument('--dff', help='delete results from an output file', action='store_true', default=False)
		parser.add_argument('--daf', help='delete all results from an ouput file', action='store_true', default=False)

		args = parser.parse_args()

		if args.sh is True:
			userInteraction.short_help(self)

		elif args.fh is True:
			userInteraction.full_help(self)

		elif args.p is True:
			# TODO
			# set the current session proxy
			pass

		elif args.mi is True:
			userInput.Credentials_Resorce(self)
			# TODO
			# add run function

		elif args.fi is True:
			userInput.Uresourcefile(self)
			# TODO
			# add run function

		elif args.dbi is True:
			# TODO
			# add run function from DB

		elif args.os is True:
			# TODO
			# set ouput to screen
			pass

		elif args.of is True:
			# TODO
			# set output to file
			pass

		elif args.odb is True:
			# TODO
			# set output to DB
			pass

		elif args.rfdb is True:
			# TODO
			# call read from DB
			pass

		elif args.dfdb is True:
			# TODO
			# call delete from DB
			pass

		elif args.dadb is True:
			# TODO
			# call delete all DB
			pass

		elif args.rff is True:
			# TODO
			# call read from file
			pass

		elif args.dff is True:
			# TODO
			# call delete from file
			pass

		elif args.daf is True:
			# TODO
			# call delete all file
			pass

	def short_help(self):
		print ''
		print ''
		print ''
		print '~! Wellcome to spYDyisai !~'
		print '''
             __
        \  /|| \\\\    _
___ ___  \/ ||  ||  |_|___ _  _
|__ |__| || ||  ||\/ | |__ |__| /_\ \/
__| |    || ||_// || | __| |  | | | ||
'''

		print '[-] spYDyishai | The google based account credentials harverster [-]'
		print ''
		print '''
-- usage flags: --

** run python spYDyishai.py with no flags for guided execution

GENRAL
* spYDyishai help       --sh
* spYDyishai help file  --hf
* set proxy             --p


USER INPUT
* run manual input      --mi
* run from file         --fi
* run from DB           --dbi

SYSTEM OUTPUT
* to screen             --os
* to flat file          --of
* to DB                 --odb

MANAGE DATA
* read from DB          --rfdb
* delete from DB        --dfdb
* delete all DB         --dadb
* read from file        --rff
* delete from file      --dff
* delete all file       --daf
'''
		quit()

	def full_help(self):
		print ''
		print '[-] spYDyishai | The google based account credentials harverster [-]'
		print '''
						-- Main help screen --

GENRAL
------
* set proxy              --p     |   set the type:ip:port of your proxy

USER INPUT
----------
[**] user and password format >	username@domain.com:password

[*] manual input        --mi     |   takes a google username and password as an initial input
[*] from file           --fi     |   takes a list of google accounts from a ' ; ' seperated  file
[*] from DB             --dbi    |   takes a list of google accounts from an existing spYDyishai DB

OUTPUT
------
[*] to screen           --os     |   prints an ongoing status and results to STDOUT
[*] to flat file        --of     |   appends the results in to a flat file
[*] to DB               --odb    |   writes the results in to a mongoDB instance

MANAGE DATA
-----------
* read from DB          --rfdb  |   read results from the DB
* delete from DB        --dfdb  |   delete results from the DB
* delete all DB         --dadb  |   delete all the resources from the DB
* read from file        --rff   |   read results from an output file
* delete from file      --dff   |   delete results from an output file
* delete all file       --daf   |   delete all results from an ouput file


EXAMPLES
--------
[*] python spYDyishai.py --mi spYDyishai@gmail.com:password -os
// this will start the credentials harvesting beginning with the manually supplied account
// and will print all results directly to the screen (STDOUT)

[*] python spYDyishai.py --mi spYDyishai@gmail.com:password ; spYDyishai2@gmail.com:password2 --of ~/spYDyishai_results
// this will start the credentials harvesting beginning with the first manually supplied account
// and will append all results to the given file

[*] python spYDyishai.py --fi ~/accounts --fo ~/spYDyishai_results --p SOCKS:1.1.1.1:8080
// this will start the credentials harvesting form all listed accoutns form the flat file
// and will append all results to the given file

[*] python spYDyishai.py --dbi localhost:27017 --odb localhost:27018
// this will start the credentials harvesting form all listed accoutns form the database
// and will write all results into a different database

[*] python spYDyishai.py --rfdb localhost:27017
// this will read all the available resource from the DB and print them to the screen

[*] python spYDyishai.py --dfdb localhost:27017 spYDyishai@gmail.com
// this will delete the spYDyishai@gmail.com file from the DB

[*] python spYDyishai.py --daf ~/spYDyishai_results
// this will delete the content of the file ~/spYDyishai_results

'''
		quit()

	def guided_wellcome(self):
		print ''
		print ''
		print ''
		print '~! Wellcome to spYDyisai !~'
		print '''
             __
        \  /|| \\\\    _
___ ___  \/ ||  ||  |_|___ _  _
|__ |__| || ||  ||\/ | |__ |__| /_\ \/
__| |    || ||_// || | __| |  | | | ||
'''
		print '''
spYDishai is a gmail spider like crawler that seeks google saved credential and allows pivoting from one account to another
until the end of all times, just feed it with initial credentials and it will do the rest.

spYDyisai will save and remember your links and credentials encrypted in a DB
and reuse them when ever it's suposed to run.

Just follow the instructions to get started..
'''
		print '[?] Would you like to read the help file before we begin? (Y/n)'
		pHelp = raw_input().lower

		while pHelp() not in ['y', 'Y', 'n', 'N', '']:
			print '[!] Please choose only "y", "n" or leave blank for default'
			pHelp = raw_input().lower

		if pHelp() in ['y', 'Y', '']:
			userInteraction.helpFile(self)
		elif pHelp() == 'n':
			userInteraction.guided_wellcome_options(self)
		else:
			print 'You broke me :/'
			quit()

	def guided_wellcome_options(self):
		print '''
[?] What would you like to do?
	[1] Provide crdentials

	[2] Read available resources from DB

	[3] Update DB resources

	[4] Delete resources from DB

	[5] Unleesh the spiders once again

	[6] Quit
		'''

		base_option = raw_input().lower
		while base_option() not in ['1', '2', '3', '4', '5', '6']:
			print '[!] Please choone only from the available options 1-6'
			base_option = raw_input().lower
		if base_option() == '1':
			userInteraction.guide(self)
			# TODO
			# dataManagement.manageDB.findDB(self)
			# dataManagement.manageDB.writeToDB(self)
			# RESET MUST STAY LAST
			userInteraction.credentialslist_reset_Q(self)
			userInteraction.guided_wellcome_options(self)
		elif base_option() == '2':
			print ''
			print '''
[?] Would you like to list all the resources in you\'re DB? (N/tb/fd)
Choose N - No, tb - Tables list, fd - Full data or leave black for default
'''
			listDB = raw_input().lower

			while listDB() not in ['n', 'N', '', 'tb', 'TB', 'fd', 'FD']:
				print '[!] Please choose only "n", "tb", "fd" or leave blank for default'
				listDB = raw_input().lower

			if listDB() in ['tb', 'TB']:
				# TODO
				# dataManagement.manageDB.readTablesFromDB(self)
				userInteraction.guided_wellcome_options(self)

			elif listDB() in ['fd', 'FD']:
				# TODO
				# dataManagement.manageDB.readTablesDataFromDB(self)
				userInteraction.guided_wellcome_options(self)

			elif listDB() in ['n', 'N', '']:
				userInteraction.guided_wellcome_options(self)
			else:
				print 'You broke me :/'
				quit()
		elif base_option() == '3':
			print '[?] What resource would you like to update?'
			# TODO
			# dataManagement.manageDB.readTablesFromDB(self)
			print '[-] Please type in the name of the resource you would like to edit'
			print ''
			# TODO
			# dataManagement.manageDB.readSingleTableData(self)
			print '[-] Please choose which value would you like to edit NONE, USERNAME or PASSWORD (NO/us/pa) or leave black for default'
			print ''
			# TODO
			# dataManagement.manageDB.editTableData(self)
			userInteraction.guided_wellcome_options(self)
		elif base_option() == '4':
			print '[!!] MAKE SURE TO TAKE COUSION WITH THIS OPTION, NO COMEING BACK FROM HERE [!!]'
			print ''
			print '[-] Please select which resource you would like to delete'
			# TODO
			# dataManagement.manageDB.deleteResourceFromDB(self)
			userInteraction.guided_wellcome_options(self)
		elif base_option() == '5':
			# TODO uleesh spiders
			print 'uleesh spiders'
			userInteraction.guided_wellcome_options(self)
		elif base_option() == '6':
			userInteraction.quit(self)


	def quit(self):
		print ''
		print '~!  ###############################################  !~'
		print 'you are blessd by the gooDYishai, keep information free.'
		print '~!  ###############################################  !~'
		print ''
		quit()

	def credentialslist_reset_Q(self):
		print ''
		print '''
######################################################################################
######################################################################################

spYDyisai is about to reset the credentialslist.ini file to it\'s default content
so that it won\'t contain any clear text credentials.

if there is any reason why you would like to keep the credentialslist.ini file as is
please choose "n", otherwise the default behaviour will be to reset the file content

######################################################################################
######################################################################################
'''
		print '[?] Would you like to cancle the content rest? (y/N)'
		content_resetYN = raw_input().lower

		while content_resetYN() not in ['y', 'Y', 'n', 'N', '']:
			print '[!] Please choose only "y", "n" or leave blacnk for default'
			content_resetYN = raw_input().lower
		if content_resetYN() in ['n', 'N', '']:
			userInteraction.credentialslist_reset(self)
			print '[!] Reset seccuessful'
		else:
			print '[!] Reset aborted'

	def guide(self):
		print ''
		print '[?] Would you like to use the credentialslist.ini file instead of the guided run? (y/N)'
		credentialslistYN = raw_input().lower

		while credentialslistYN() not in ['y', 'Y', 'n', 'N', '']:
			print '[!] Please choose only "y", "n" or leave blacnk for default'
			credentialslistYN = raw_input().lower
		if credentialslistYN() in ['y', 'Y']:
			print ''
			print '[-] Looking for credentialslist.ini'
			userInteraction.credentialslist_find(self)
		else:
			print ''
			print '[-]Moveing forward with guided run.'

			userInteraction.credentialslist_clear(self)

			print ''
			print '[?] How many resources would you like to add?'
			global resource_number
			resource_number = raw_input()
			while not resource_number.isdigit():
				print '[!] Please only use numbers.'
				print '[?] How many resources would you like to add?'
				resource_number = raw_input()

			resource_number = int(resource_number)
			if resource_number in range (1,6):
				for resource_number in range(resource_number):
					userInput.Credentials_Resorce(self)
			elif resource_number in range (6,11):
				print '[?] ' +str(resource_number)+ ' Is a large number, are you sure you\'re going to add ' +str(resource_number)+ ' resources? (y/N)'
				resourceNumYN = raw_input().lower
				while resourceNumYN() not in ['y', 'Y', 'n', 'N', '']:
					print '[!] Please choose only "y", "n" or leave blank for default'
					resourceNumYN = raw_input().lower
				if resourceNumYN() in ['y','Y']:
					for resource_number in range(resource_number):
						userInput.Credentials_Resorce(self)
				elif resourceNumYN() in ['n', 'N', '']:
					userInteraction.guide(self)
			elif resource_number < 1:
				print ''
				print '[!] Since you\'re not adding any resources, manually or via the credentialslist.ini file i\'ll be quiting now'
				print ''
				pass
			else:
				print ''
				print '[!] For so manny resources please use the credentialslist.ini'
				print '[!] the default location should be: ' +self.credentialslist_location
				quit()

	def credentialslist_find(self):
		if os.path.isfile(self.credentialslist_location+"/"+self.credentialslist_filename) == False:
			print '[!] spYDyisai could not find the credentialslist.ini file in it\'s default location'
			print ''
			print '[?] Would you like to provide the Full Path for the credentialslist.ini file'
			print 'or would you perffere going back to the Guided Run? (FP/gr)'
			fpgr = raw_input().lower

			while fpgr() not in ['fp', 'FP', 'gr', 'GR', '']:
				print '[!] Please choose only "fp" for Full Path or "gr" for Guided Run or leave blank for default (FP)'
				fpgr = raw_input().lower

			if fpgr() in ['fp', 'FP', '']:
				userInput.Uresourcefile(self)
			elif fpgr() in ['gr', 'GR']:
				userInteraction.guide(self)
		else:
			userInteraction.credentialslist_read(self)

	def credentialslist_read(self):
		if os.path.isfile(self.credentialslist_location+"/"+self.credentialslist_filename) == True:
			print ''
			print '[-] Found credentialslist.ini.'
		elif os.path.isfile(userFilePath+"/"+self.credentialslist_filename) == True:
			print ''
			print '[-] Found credentialslist.ini.'
		else:
			pass

	def credentialslist_reset(self):
		try:
			credentialslist = open(self.credentialslist_location+"/"+self.credentialslist_filename, 'w', 0)
			original_credentialslist = '''
[resource0]
username = username
password = password

[resource1]
username = None
password = None
'''
			credentialslist.write(original_credentialslist)
			credentialslist.close()
		except:
			credentialslist = open(userFilePath+"/"+self.credentialslist_filename, 'w', 0)
			original_credentialslist = '''
[resource0]
username = username
password = password

[resource1]
username = None
password = None
'''
			credentialslist.write(original_credentialslist)
			credentialslist.close()

	def credentialslist_clear(self):
		credentialslist = open(self.credentialslist_location+"/"+self.credentialslist_filename, 'w', 0)
		clear_content = ''
		credentialslist.write(clear_content)
		credentialslist.close()




if __name__ == '__main__':
	try:
		UI = userInteraction()
		if len(sys.argv) > 1:
			wellcome = UI.wellcome()
		else:
			guided_wellcome = UI.guided_wellcome()
	except KeyboardInterrupt:
		print ''
		print ''
		print '~!  ###############################################  !~'
		print 'you are blessd by the gooDYishai, keep information free.'
		print '~!  ###############################################  !~'
		print ''
		quit()
