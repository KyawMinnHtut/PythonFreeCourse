from mysql.connector import connector, error

try:
    with connect(
        host="localhost",
        user="root",
        password = "",
        database = "python_free_course"
    ) as connection:
        print(connection)
        #Insert query
        title = input("Enter title : ")
        description = input("Enter description : ")
        year = input("Enter year : ")
        sql = "INSERT INTO movie(title, description, year) values ()"
        with connection.cursor() as cursor:
            cursor.execute(sql)
            connection.commit()
        #Select query
        sql = "SELECT * from movie;"
        with connection.cursor() as cursor:
            cursor.execute(sql)
            for movie in cursor.fetchall():
                print(movie)
except Error as err:
    print(err)