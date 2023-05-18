from low_level_commands import *

# Adds Data to Database  
# Parameters are: 'table_name' = the name of table and 'inputs' = data for each column in order
def add_data(table_name, inputs):
    result = table_structure_nokey(table_name)
    user_inputs = inputs

    column_names = result

    # function in envVars.py that setups database connection and sends parameter as SQL command
    edit_database(f"""INSERT INTO {table_name} ({column_names}) VALUES ({user_inputs});""")

def remove_data(table_name, key, admin):
    if check_admin(admin) == True:
        table_column = get_primary_column(table_name)
        table_column = table_column.replace("'", "")
        edit_database(f"DELETE FROM {table_name} WHERE {table_column} = {key};")
        return "Success! New Data Added."
    else:
        return "Error, User does not have permission to remove data"

def edit_data(table_name, key, column, edit):
    key_column = get_primary_column(table_name)

    edit_database(f"""UPDATE {table_name} SET {column} = '{edit}'
                WHERE {key_column} = {key}; """)


def open_file(file_name):
    file_path = file_name
    if platform.system() == 'Darwin':       # macOS
        subprocess.call(('open', file_path))

    elif platform.system() == 'Windows':    # Windows
        os.startfile(file_path)
        
    else:                                   # linux variants
        subprocess.call(('xdg-open', file_path))    

#array_test = ["mommm", "9581", "0"]    


# mysql.connector.errors.DatabaseError This error must be handled at the main_functions level, not at the lower level error catcher


#print(get_primary("user_names", "ID", "matt"))
#print(get_primary_column("user_names"))
#remove_data("user_names", "10")


#edit_data("logins", "21", "user", "matt")

