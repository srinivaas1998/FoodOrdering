import psycopg2


def create_table():
    sql = "create table cust(name varchar(100), phone_no varchar(10), password varchar(20),location_cust point, location_rest point, distance numeric);"

    conn = None
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect("dbname=food user=postgres password=chinku port=5432")
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql)

        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def insert_entry(name, phone, password, lat, long, latr, longr):
    sql = """INSERT INTO cust(name,phone_no,password,location_cust,location_rest)
                 VALUES(%s,%s,%s,'(%s,%s)','(%s,%s)') ;"""
    conn = None
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect("dbname=food user=postgres password=chinku port=5432")
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (name, phone, password, float(lat), float(long), latr, longr))

        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def update_distance():

    # A* Distance uses Euclidean as Heuristics.
    sql = """ update cust set distance=(select ST_Distance(geometry(location_cust),geometry(location_rest)) 
              from cust) """

    conn = None

    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect("dbname=food user=postgres password=chinku port=5432")
        # create a new cursor
        cur = conn.cursor()
        # execute the UPDATE  statement
        cur.execute(sql)
        # get the number of updated rows
        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def select():
    conn = None
    par = ""


    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect("dbname=food user=postgres password=chinku port=5432")
        # create a new cursor
        cur = conn.cursor()
        sql = "SELECT distance from cust"
        # execute the UPDATE  statement
        cur.execute(sql)
        par = cur.fetchone()[0]
        # get the number of updated rows

        # Commit the changes to the database
        conn.commit()
        # Close communication with the PostgreSQL database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return par




def drop_table():
    sql = "drop table cust"
    conn = None
    try:
        # connect to the PostgreSQL database
        conn = psycopg2.connect("dbname=food user=postgres password=chinku port=5432")
        # create a new cursor
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql)

        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()



