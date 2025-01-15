import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
from Base.logfile import Logger

log=Logger().get_logger()

load_dotenv()
host=os.getenv("DB_HOST")
database=os.getenv("DB_DATABASE")
user=os.getenv("DB_USER")
password=os.getenv("DB_PASSWORD")

class Omnify_connect():
    @staticmethod
    def omnify_connection():
        try:
            connection = mysql.connector.connect(host=host,
                                                database=database,
                                                user=user,
                                                password=password)
            if connection.is_connected():
                return connection
            
        except Error as e:
            print("Error while connecting to MySQL", e)
            return None

    def fetch_data(self,query):
        try:
            connection=self.omnify_connection()
            
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute(query)
                record = cursor.fetchall()
                print("Record fetched successfully ")
                return record
        
        except Error as e:
            log.warning("Error while connecting to MySQL", e)
        
        finally:
            if connection and (connection.is_connected()):
                connection.close()
                print("MySQL connection is closed")

    def update_data(self,query):
        try:
            connection=self.omnify_connection()
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute(query)
                connection.commit()
                print("Record Updated successfully ")

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if connection and (connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")

    def delete_data(self,query):
        try:
            connection=self.omnify_connection()
            if connection.is_connected():
                cursor = connection.cursor()
                cursor.execute(query)
                connection.commit()
                print("Record Deleted successfully ")

        except Error as e:
            print("Error while connecting to MySQL", e)

        finally:
            if connection and (connection.is_connected()):
                cursor.close()
                connection.close()
                print("MySQL connection is closed")