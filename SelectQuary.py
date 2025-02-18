import psycopg2


def SelectQuary():
    try:
        connection = psycopg2.connect(
            user="test",
            password="test",
            host="localhost",
            port="5432",
            database="test" 
        )
        cursor = connection.cursor()

        pg_select = """ SELECT * FROM public."h3" """

        cursor.execute(pg_select)

        DB_records = cursor.fetchall()
        print("Records of row in the table")
        for row in DB_records:
            print (row[0], '- xxxxx')
            print ('price', row[1], '$')
            print ('size', row[2], 'm2\n---')
        return DB_records

    except (Exception, psycopg2.Error) as error:
        print("Error selecting data from table h1", error)
        connection = None

    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("The PostgreSQL connection is now closed")