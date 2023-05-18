from envVars import *
import logging
import os
import datetime
import subprocess
import platform

# Retrieves primary key for specific row, requires 3 parameters: table name, primary key column name, and search value

def get_primary(table_name, retrieve_key, user_input):
    result = (retrieve_info(f"""SELECT {retrieve_key} FROM {table_name} WHERE uname = '{user_input}';"""))
    return result

# Retrieves name of the primary key column for a table

def get_primary_column(table_name):
    column_name = retrieve_info(f"""SELECT k.COLUMN_NAME
                    FROM information_schema.table_constraints t
                    LEFT JOIN information_schema.key_column_usage k
                    USING(constraint_name,table_schema,table_name)
                    WHERE t.constraint_type='PRIMARY KEY'
                    AND t.table_schema=DATABASE()
                    AND t.table_name='{table_name}';""")
    column_name = format_string(column_name)
    column_name = column_name.replace(",", "")
    column_name = column_name.replace("'", "")
    return column_name

# Retrieves all column names besides primary key, important for adding new data
def table_structure_nokey(table):
    column_names = ''
    output = query(f"SELECT `COLUMN_NAME` FROM `information_schema`.`COLUMNS` \
                   WHERE (`TABLE_NAME` = '{table}') AND (`COLUMN_KEY` <> 'PRI')")
    for i in range(len(output)):
        column_names += f"{output[i][0]}, " 
    column_names = column_names[:-2]
    result = (column_names)
    return result

# Retrieves all column names for a table

def table_structure_all(table):
    column_names = ''
    output = query(f"SELECT `COLUMN_NAME` FROM `information_schema`.`COLUMNS` \
                   WHERE (`TABLE_NAME` = '{table}')")
    for i in range(len(output)):
        column_names += f"{output[i][0]}, " 
    column_names = column_names[:-2]
    result = (column_names)
    return result

# Retreives amount of columns for a table
def table_amount_columns(table):
    output = query(f"SELECT `COLUMN_NAME` FROM `information_schema`.`COLUMNS` \
                   WHERE (`TABLE_NAME` = '{table}') AND (`COLUMN_KEY` <> 'PRI')")
    result = len(output)
    return result

# formats arrays into strings that follow SQL syntax
def convert_array(array):
    converted_string = ""
    for i in range(len(array)):
        converted_string += f"'{array[i]}', "
    converted_string = converted_string[:-2]
    if '(' or ')' in converted_string:
        converted_string = converted_string.replace('(', "'")
        converted_string = converted_string.replace(')', "'")

    return converted_string

# formats string by removing any ()

def format_string(user_input):
    converted_string = user_input
    if '(' or ')' in converted_string:
        converted_string = converted_string.replace('(', "")
        converted_string = converted_string.replace(')', "")
    return converted_string

# Checks if user has admin privledges, needed for actions deemed potentially abuseable 

def check_admin(admin):
    if admin == 0 or admin == "0":
        return True
    else:
        return False
    
# Stores all encountered errors to troubleshoot easier

def error_depository(error):
    error_array = [("Row doesn't exist", mysql.connector.errors.IntegrityError), ("Column name wrong", mysql.connector.errors.ProgrammingError), ("Database could not be reached", mysql.connector.errors.DatabaseError)]

# Creates an error log in case an unknown error is encountered

def create_error_log(error_cmd):
    cwd = os.getcwd()
    targetPath = os.path.join(cwd, 'Crash_Logs')
    while not os.path.exists(targetPath):
        os.mkdir(targetPath)
    
    current_date_time = f"{datetime.datetime.now()}"
    current_date_time = current_date_time[:-10]
    current_date_time = current_date_time.replace(':', '-')

    targetFile = os.path.join(targetPath, f'log_{current_date_time}.log')
    open(targetFile, 'w')
    logging.basicConfig(level=logging.DEBUG, filename = f'Crash_Logs/log_{current_date_time}.log')
    logging.exception("Error!")
    return f"Crash log, log_{current_date_time}.log has been created at {targetPath}"



