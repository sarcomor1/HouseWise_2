import psycopg2


def DeleteQuary(number):
    try:
        connection = psycopg2.connect(
            user="test",
            password="test",
            host="localhost",
            port="5432",
            database="test"
        )
        cursor = connection.cursor()

        pg_delete = """ DELETE FROM public."h3" WHERE "id" = %s"""

        delete_values = (str(number))
        cursor.execute(pg_delete, delete_values)
        connection.commit()
        count = cursor.rowcount
        print("successfully deleted", count, "rows.")

    except (Exception, psycopg2.Error) as error:
        print("Error in Deleting the data", error)
        connection = None

    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("The PostgreSQL connection is now closed")