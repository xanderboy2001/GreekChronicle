import platform
from main_functions import *
from main import *

def bootup():
    i = 1
    while i != 0:
        x = str(input("Enter an action to commit or enter 0 to quit: ")) 
        if x == "0":
            i = 0
        else:
            msg = check_success(x)
            if msg is None:
                print("Success!")
            else:
                print(msg)



def check_success(x):
    try:
        exec(x)
    except mysql.connector.errors.IntegrityError:
        return "Error, Data already exists"
    except mysql.connector.errors.ProgrammingError:
        return "Error, table structure incorrect (Usually means a column name was incorrect.)"
    except mysql.connector.errors.DatabaseError:       
        return "Error, database could not be reached. (Server is not running or firewall may be interfering)"
    except NameError:
        return "Unknown input was entered"
    except KeyboardInterrupt:
        return "Program recieved exit command, shutting down..."
    #except SyntaxError:
        #return "Error, invalid action attempted by program. Something has gone wrong with the code!"
    except:
        error_msg = str(create_error_log(x))
        print("Unspecified Error has occurred, a crash log will now be created...\n")
        return error_msg

# File must be placed in directory before the MySQL Server!

def main():
    try:
        if platform.system() == 'Windows':
            cmd = "Portable_Server/usbwebserver.exe"
            process = subprocess.Popen(cmd, stdout=subprocess.PIPE, creationflags=0x08000000)
        mainmain()
        result = bootup()
        print("\nProgram recieved exit command, shutting down...")
    except KeyboardInterrupt:
        print("\nProgram recieved exit command, shutting down...")
    if platform.system() == 'Windows': 
        process.kill()
        process.wait()


#remove_data("logins", "26", 0)
#"(add_data('logins', array_test))"
#edit_data("logins", "27", "user", "matt")