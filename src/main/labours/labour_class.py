# from loguru import logger
# from src.main.databases.mysql_connector import MySqlConnection, MySQLCRUDOperation
# import configparser
# from src.main.databases.mysql_connector import *
# from main.utility.encrypt_decrypt import decrypt
# from datetime import datetime






#     def __save_to_database(self, crud):
#         query = f"SELECT id FROM labours WHERE lower(first_name) = '{self.first_name}' AND lower(last_name) = '{self.last_name}' "
#         logger.info(f"{query}")
#         result = crud.read_from_mysql(query)

#         if result:
#             logger.info(f"Labour already exists with ID: {result[0][0]}")
#             return result[0][0]
#         logger.info(f"{self.email}")
#         insert_query = f"""
#             INSERT INTO labours (first_name, last_name, wage, role, email)
#             VALUES ('{self.first_name}', '{self.last_name}', {self.wage},'{self.role}','{self.email}')
#         """
#         logger.info(f"{insert_query}")

#         crud.insert_into_mysql(insert_query)

#         result = crud.read_from_mysql(query)
#         logger.info(f"New labour added with ID: {result[0][0]}")
#         return result[0][0]

#     @staticmethod
#     def login_and_logout(crud, id=None, first_name=None, last_name=None):
        # if id is None:
        #     if first_name is None or last_name is None:
        #         logger.error("Please provide either id or first name and last_name")
        #         return
            
        #     query = f"""
        #             select id from labours
        #             WHERE lower(first_name) = '{first_name.lower()}' 
        #             AND lower(last_name) = '{last_name.lower()}' 
        #             """
        #     try:
        #         result = crud.read_from_mysql(query)
        #         id = result[0][0]
        #         logger.info(f"Id from labours table {result[0][0]}")
        #     except IndexError as err:
        #         logger.error("Please register yourself. No entry found")
        #         raise err
        #     except Exception as e:
        #         logger.error("Got error {e}")

        # current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # current_date = datetime.now().strftime('%Y-%m-%d')

        # check_query = f"""
        #     SELECT id, start_time, end_time FROM attendance
        #     WHERE labour_id = {id} AND DATE(start_time) = '{current_date}'
        # """
        
        # result = crud.read_from_mysql(check_query)
        # logger.info(f"Data from labours table {result}")

        # if len(result) == 0:
        #     insert_query = f"""
        #     INSERT INTO attendance (labour_id, start_time)
        #     VALUES ({id}, '{current_time}')
        #     """
        #     crud.insert_into_mysql(insert_query)
        #     logger.info(f"Labour {id} logged in at {current_time}")
        # else:
        #     id = result[0][0]
        #     update_query = f"""
        #             UPDATE attendance
        #             SET end_time = '{current_time}'
        #             WHERE id = {id}
        #         """
        #     crud.insert_into_mysql(update_query)
        #     logger.info(f"Labour {id} logged out at {current_time}")
            

