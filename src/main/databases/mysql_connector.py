import mysql.connector
from loguru import logger



class MySqlConnection:
    _instance = None  # Singleton instance

    def __init__(self, config):
        if MySqlConnection._instance is not None:
            raise Exception("Use get_instance() instead of creating a new object.")

        self.config = config
        self.connection = None
        self.connect()
    
    @classmethod
    def get_instance(cls, config=None):
        if cls._instance is None:
            cls._instance = cls(config)
        return cls._instance

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.config["mysql_database"]["host"],
                user=self.config["mysql_database"]["user"],
                password=self.config["mysql_database"]["password"],
                database=self.config["mysql_database"]["database"]
            )
            logger.info("MySQL Connection successful")
        except Exception as e:
            logger.error(f"Database connection error: {e}")
            raise e

    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            logger.info("MySQL Connection closed")


























# from loguru import logger
# import mysql.connector
# from main.utility.encrypt_decrypt import decrypt


# class MySqlConnection:
#     def __init__(self,config):
#         self.config = config
#         self.connection = None


#     def connect(self):
#         try:
#             self.connection = mysql.connector.connect(host = self.config["mysql_database"]["host"],
#                             user = self.config["mysql_database"]["user"],
#                             password = self.config["mysql_database"]["password"],
#                             database = self.config["mysql_database"]["database"])
#             logger.info("MySQL Connection succesful")

#         except Exception as e:
#             logger.error(f"Error occured: {e}")
#             raise e
        
#     def close(self):
#         if self.connection.is_connected():
#             self.connection.close()
#             logger.info("MySQL Connection closed")
        

# class MySQLCRUDOperation:
#     def __init__(self,mysql_connection):
#         self.connection = mysql_connection 

#     def read_from_mysql(self,query):
#         logger.info(f"Query sent to read {query}")
#         try:
#             cursor = self.connection.cursor()
#             cursor.execute(query)
#             result = cursor.fetchall()
#             return result
#         except Exception as e:
#             logger.info(f"Error occured in mysql query run {e}")
#             raise e
#         finally:
#             if cursor:
#                 cursor.close()
#                 logger.info("Cursor closed")

#     def insert_into_mysql(self,query):
#         logger.info(f"Query sent to Insert the data {query}")
#         try:
#             cursor = self.connection.cursor()
#             cursor.execute(query)
#             result = cursor.fetchall()
#             return result
#         except Exception as e:
#             logger.info(f"Error occured in mysql query run {e}")
#             raise e
#         finally:
#             self.connection.commit()


