import pymysql
from config import *
#import urllib.parse as up


class MySQLServer:
	def __init__(self):
		try:
			self.connection = pymysql.connect(
				host=HOST,
				port=PORT,
				user=user,
				password=password,
				database="bank",
				cursorclass=pymysql.cursors.DictCursor)

			print('Connected successfully...')

			self.cursor = self.connection.cursor()

		except Exception as ex:
			print('Connected refused...')
			print(ex)

	def disconnect_db(self):
		self.connection.close()
		print("Disconnection...")

	def insert_data_users(self, login, passw):
		try:
			self.cursor.execute(f"insert users(login, passw) values('{login}', '{passw}')")

		except Exception as ex:
			print("Cannot insert the data...")
			print(ex)

		else:
			self.connection.commit()

	def insert_data_clients(self, firstname, lastname, fathername, age, passport):
		try:
			self.cursor.execute(f"insert clients values ('{firstname}', '{lastname}', '{fathername}', {age}, '{passport})'")

		except Exception as ex:
			print("Cannot insert the data...")
			print(ex)

		else:
			self.connection.commit()

	def insert_data_account(self, money, name_currency):
		try:
			self.cursor.execute(f"insert bank_account values('{name_currency}', '{money}')")

		except Exception as ex:
			print("Cannot insert the data...")
			print(ex)

		else:
			self.connection.commit()

	def account_refill_debiting (self, money, user_id):
		try:
			self.cursor.execute(f"update bank_account set money = money + {money} where user_id = {user_id}")
		except Exception as ex:
			print("Ошибка: " + ex)
		else:
			self.connection.commit()

	def delete_data_users(self, data):
		result = self.search_user(data)
		self.cursor.execute(f"delete from users where user_id = {result[0].get('user_id')}")
		self.connection.commit()

	def search_user(self, data):
		if isinstance(data, int):
			try:
				self.cursor.execute(f"select * from users where user_id = {data}")
			except Exception as ex:
				print("Ошибка: " + ex)
			else:
				result = self.cursor.fetchall()
				return result
		else:
			try:
				self.cursor.execute(f"select * from users where login = '{data}'")
			except Exception as ex:
				print("Ошибка: " + ex)
			else:
				result = self.cursor.fetchall()
				return result

	def search_client(self, data):
		if isinstance(data, int):
			try:
				self.cursor.execute(f"select * from clients where user_id = {data}")
			except Exception as ex:
				print("Ошибка: " + ex)
			else:
				result = self.cursor.fetchall()
				return result
		else:
			try:
				self.cursor.execute(f"select * from clients where firstname = '{data}'")
			except Exception as ex:
				print("Ошибка: " + ex)
			else:
				result = self.cursor.fetchall()
				return result

