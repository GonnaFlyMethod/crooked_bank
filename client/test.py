from sql_wrapper import MySQLServer

login = "user2"
password = "user"

table_worker = MySQLServer()
table_worker.delete_data_users(login)
table_worker.disconnect_db()
#able_worker.insert_data_users(login, password)
