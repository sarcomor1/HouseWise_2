import psycopg2


def InsertQuary(price, size):
    try:
        connection = psycopg2.connect(
            user="test",
            password="test",
            host="localhost",
            port="5432",
            database="test"
        )
        cursor = connection.cursor()

        pg_insert = """ INSERT INTO public."h3" ("price", "size") VALUES(%s, %s)"""

        inserted_values = (price, size)

        cursor.execute(pg_insert, inserted_values)

        connection.commit()

        count = cursor.rowcount
        print("successfully inserting", count, "records.")

    except (Exception, psycopg2.Error) as error:
        print("Error connection to PostgreSQL database", error)
        connection = None

    finally:
        if (connection):
            cursor.close()
            connection.close()
            print("The PostgreSQL connection is now closed")