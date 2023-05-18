from os import getcwd
from os.path import join
import mysql.connector

# These variables get used quite often, so I put them here

CWD = getcwd()
#CWD = join(CWD, 'GreekChronical')
DESIGNER_PATH = join(CWD, 'Designer_Files')
member_attrs = ["Name", "Big", "Date of Birth", "Date Joined"]
file_attrs = ["Name", "Location", "Date Created", "Date Modified"]

# Make query to database
def query(query):
    # Configures connection
    connection = mysql.connector.connect(host="localhost", port=3307, user='admin', passwd='1234', database="portable_test")
    cursor = connection.cursor(buffered=True)
    # Executes the query
    cursor.execute(query)
    # Gets all results
    result = cursor.fetchall()
    # Closes the conenctions
    cursor.close()
    connection.close()
    return result

def edit_database(user_input):
    connection = mysql.connector.connect(host="localhost", port=3307, user='admin', passwd='1234', database="portable_test")
    cursor = connection.cursor()
    try:
        cursor.execute(user_input)
        connection.commit()
    except:
        raise

    cursor.close()
    connection.close()

def retrieve_info(user_input):
    connection = mysql.connector.connect(host="localhost", port=3307, user='admin', passwd='1234', database="portable_test")
    cursor = connection.cursor()
    result = ""
    try:
        cursor.execute(user_input)
        for x in cursor:
            result += str(x)
        connection.commit()
    except:
        connection.rollback()
    cursor.close()
    connection.close()
    return result

# Checks if operation was successful, 0 = add, 1 = edit, 2 = remove
"""
def check_success(input):
        try:
            edit_database(input)
        except mysql.connector.errors.IntegrityError:
            return "Error, Data already exists"
        except mysql.connector.errors.ProgrammingError:
            return "Error, table structure incorrect (Usually means column name was incorrect.)"
        except mysql.connector.errors.DatabaseError:         
            return "Error, database could not be reached. (Server is not running or firewall may be interfering)"
        except:
            raise

#count = edit_database(input)
#if count < 1:

# Add Functionality into GUI to then ask if they would like to add the data they were trying to edit!

"""