import os
import mysql.connector
from envVars import *
from main_functions import *

class UserObject():
    # Initializes user with given username and encoded password
    def __init__(self, uname, psswd, perms):
        self.uname = str(uname)
        self.psswd = str(psswd)
        # Database reads permission flag as 1/0
        if perms:
            self.canWrite = 1
        else:
            self.canWrite = 0
        # saves user to db
        save_user(self)

def save_user(user):
    # Creates sql statement with given variables
    person = [user.uname, user.psswd, user.canWrite]
    # Executes sql statement and commits to the db
    add_data('logins', person)

def read_userList():
    # Gets a list of all users
    userList = query("SELECT user, pass, privledge FROM logins;")
    return userList

def findUser(uname):
    # Pulls information about a given user
    sql=f"SELECT * FROM logins WHERE user = '{uname}';"
    query(sql)

def exists(uname):
    # checks if user exists
    sql=f"SELECT * FROM logins WHERE user = '{uname}';"
    result = query(sql)
    if result != []:
        return True
    else:
        return False
    
def authenticate(username, password):
    # uses username to pull password from db, then checks given passwd against db password
    # returns true or false
    user_info = query(f"SELECT * FROM logins WHERE user = '{username}';")
    print("USER INFO: ", user_info)
    saved_psswd = user_info[0][2]
    return password == saved_psswd