import csv
from multiprocessing import connection
import os
import pymysql
import logging


logger = logging.getLogger()
logger.setLevel(logging.INFO)

def database_insert(table_name, values):
    try:
        conn = get_database_connection()
        if conn != None:
            curr = conn.cursor()
            sql = """insert into `%s` (response_id, response_family_id, 
            user_id, username, location, submitted_time, synced_time, last_modified_time,
            name, email, mobile_number, gender, age, 
            monthly income, monthly savings, 
            monthly expenditure, monthly food expenditure, montly cable expenditure, monthly healthcare expenditure, monthly fuel expenditure) 
            values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %d, %d, %d, %d, %d, %d, %d, %d) """
            curr.execute(sql, \
                (table_name, values[0], values[1], values[2], values[3], values[4], values[5], \
                    values[6], values[7], values[8], values[9], values[10], values[12], \
                        values[13], values[14], values[15], values[16], values[17], values[18], values[19]))

            conn.commit()
            conn.close()
    except Exception as e:
        logger.error(e)
       

def database_table_select_all_values(table_name):
    try:
        conn = get_database_connection()
        if conn != None:
            curr = conn.cursor()
            sql = """select * from %s"""
            curr.execute(sql, (table_name))

            csv_statement_file = "./data/google_sheet_data.csv"
            output_csv_file = open(csv_statement_file, 'w', encoding='utf-8')
            csv_output = csv.writer(output_csv_file)

            for row in curr:
                csv_output.writerow(row)
            
            output_csv_file.close()

    except pymysql.MySQLError as e:
        logger.error(e)

def get_database_connection():
    try:
        connection = pymysql.connect(
            host=os.getenv("RDS_HOST"), user=os.getenv("RDS_USERNAME"), passwd=os.getenv("RDS_PASSWORD"), db=os.getenv("RDS_DB_NAME"), connect_timeout=5)
        return connection
    except pymysql.MySQLError as e:
        logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
        logger.error(e)
        return None