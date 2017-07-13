#!/usr/bin/python

"""
Funcion: Select a random user from the user pool while attching him/her with a given comment.

Usage: python ./UserSelector.py

Author: zidongzhang

Update: 2016-07-12 20:28:32

"""

import random

class UserSelector:
	"""
	Select a random user from the user pool while attaching his/her information with a given comment.
	"""

	def __init__(self, file_name):
		"""
		Get information of a random user 
		"""
		openfile = open(file_name, "r")		
		self.__user_pool = openfile.readlines()
		openfile.close()

		return


	def random_pick_user(self, commentlist):
		"""
		Randomly pick an user and collect his/her information(including username, userid and profile picture).
		"""

		for comment in commentlist:
			user = random.choice(self.__user_pool)
			user_info = user.split()
			user_name = user_info[0]
			user_id = user_info[1]
			user_picture = user_info[2]
			"""
			user_info: user's information(including username, userid and profile picture)
			"""

			print user_name,user_id,user_picture,comment

		return

		
if __name__ == "__main__":
	"""
	Data testing section (Will not run if using UserSelector as a class).
	"""

	user_selector = UserSelector("writefilefinal02.txt")
	test_commentlist = ["commnet1", "comment2", "comment3"]

	user_selector.random_pick_user(test_commentlist)
