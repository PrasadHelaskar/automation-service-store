import os
import mysql.connector
from dotenv import load_dotenv
from base.logfile import Logger

log=Logger().get_logger(__name__)

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
                # log.info("Connected > "+str(connection.is_connected()))
                return connection
            
        except Exception as e:
            log.error("Error while connecting to MySQL"+str(e))
            return None

    def fetch_data(self,query):
        # log.info("Query > "+str(query))
        try:
            connection=self.omnify_connection()
            if connection and connection.is_connected():
                cursor = connection.cursor()
                cursor.execute(query)
                record = cursor.fetchall()
                # log.info("Record fetched successfully")
                return record
        
        except Exception as e:
            log.error("Error while connecting to MySQL"+str(e))
        
        finally:
            if connection and (connection.is_connected()):
                connection.close()
                # log.info("MySQL connection is closed")

    def update_data(self,query):
        try:
            connection=self.omnify_connection()
            if connection and connection.is_connected():
                cursor = connection.cursor()
                cursor.execute(query)
                connection.commit()
                log.info("Record Updated successfully")

        except Exception as e:
            log.error("Error while connecting to MySQL"+str(e))

        finally:
            if connection and (connection.is_connected()):
                cursor.close()
                connection.close()
                log.info("MySQL connection is closed")

    def delete_data(self,query):
        try:
            connection=self.omnify_connection()
            if connection and connection.is_connected():
                cursor = connection.cursor()
                cursor.execute(query)
                connection.commit()
                log.info("Record Deleted successfully")

        except Exception as e:
            log.error("Error while connecting to MySQL"+str(e))

        finally:
            if connection and (connection.is_connected()):
                cursor.close()
                connection.close()
                log.info("MySQL connection is closed")