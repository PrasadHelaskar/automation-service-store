import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()
host=os.getenv("db_host")
database=os.getenv("db_database")
user=os.getenv("db_user")
password=os.getenv("db_password")

class Omnify_connect():
    def fetch_data(self,query):
        try:
            connection = mysql.connector.connect(host=host,
                                                database=database,
                                                user=user,
                                                password=password)
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute(query)
                record = cursor.fetchall()
                print("Record fetched successfully ")
                return record

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

    def update_data(self,query):
        try:
            connection = mysql.connector.connect(host=host,
                                                database=database,
                                                user=user,
                                                password=password)
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute(query)
                connection.commit()
                print("Record Updated successfully ")

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

    def delate_data(self,query):
        try:
            connection = mysql.connector.connect(host=host,
                                                database=database,
                                                user=user,
                                                password=password)
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute(query)
                connection.commit()
                print("Record Deleted successfully ")

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if (connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")