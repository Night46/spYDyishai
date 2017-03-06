# # This is the structure to use as base for this module
#
# import requests
# from bs4 import BeautifulSoup
#
# login = "spYDyishai@gmail.com"
# pwd = ""
#
# url_login = "https://accounts.google.com/ServiceLogin"
# url_auth = "https://accounts.google.com/ServiceLoginAuth"
#
# session = requests.session()
# login_html = session.get(url_login)
#
# soup = BeautifulSoup(login_html.content)
# form = soup.find('form')
# all_inputs = form.findAll('input')
#
# my_dict = {}
# for u in all_inputs:
#     if u.has_attr('value'):
#         my_dict[u['name']] = u['value']
# my_dict['Email'] = login
# my_dict['Passwd'] = pwd
#
# session.post(url_auth, data=my_dict)
#
# print session.get("https://mail.google.com").text
#



# ##############################################################################
#
#	Imports
#
# ##############################################################################

import dataManagement
import pymongo

# ##############################################################################
#
#	Main
#
# ##############################################################################

class connection_initiation():
	def __init__(self):
		pass


class google_connect(connection_initiation):
	def check_login_url(self):
		pass

	def set_proxy(self):
		pass

	def web_connect(self):
		pass


	def web_login(self):
		pass

	def web_logout(self):
		pass


class google_explore(connection_initiation):
	def current_id(self):
		pass

	def current_location(self):
		pass

	def credentials_location(self):
		pass


class harvester(connection_initiation):
	def cred_collector(self):
		pass

	def cred_tmp_orgenizer(self):
		pass

if __name__ == '__main__':
	pass
