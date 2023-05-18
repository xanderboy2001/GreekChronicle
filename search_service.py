from envVars import query
from ImageObject import ImageObject
from DocObject import DocObject
from MemberObject import MemberObject

def search(search):

    tables = ['image', 'doc', 'member']
    main_result = []
    lower_search = search.lower()

    for table in tables:
        # Creates query
        if table == 'member':
            sql_query = f"SELECT * FROM {table} WHERE name LIKE '%{lower_search}%' \
                OR big LIKE '%{lower_search}%' \
                OR bdate LIKE '%{lower_search}%' \
                OR join_date LIKE '%{lower_search}%'"
        else:
            sql_query = f"SELECT * FROM {table} WHERE name LIKE '%{lower_search}%' \
                OR location LIKE '%{lower_search}%'"

        print("Executed query: " + sql_query)

        result = query(sql_query)
        
        # Creates object based on table
        for data in result:
            if table == 'image':
                id = data[0]
                name = data[1]
                location = data[2]
                create = data[3]
                modify = data[4]
                object = ImageObject(id,name,location,create,modify)
            elif table == 'doc':
                id = data[0]
                name = data[1]
                location = data[2]
                create = data[3]
                modify = data[4]
                object = DocObject(id,name,location,create,modify)
            elif table == 'member':
                member_id = data[0]
                name = data[1]
                big = data[2]
                mentor_id = data[3]
                bdate = data[4]
                join_date = data[5]
                object = MemberObject(member_id, name, big, mentor_id, bdate,join_date)
            
            main_result.append(object)
        print("Object: ", object)

    print("Main result: ", main_result)

    return main_result          

def test_connection():
    result = query("SELECT * FROM image")
    print("Query results for test: " , result)


#test_connection()
search("a")