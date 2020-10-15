import pyodbc
import pandas as pd


# def get_data():
#
#     # CONNECT TO ACCESS DB
#     conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};'
#                           r'DBQ=/apps/app_repo/flaskapp/production_db.accdb'
#                           )
#
#                           # r'DBQ=C:\Users\joelb\Documents\Development\production_test\flaskapp\production_db.accdb;')
#
#     # BASE SQL
#     sql = f"""SELECT *
#               FROM person
#           """
#     # CONVERT SQL TO PANDAS
#     person_df = pd.read_sql(sql, conn)
#
#     return person_df


