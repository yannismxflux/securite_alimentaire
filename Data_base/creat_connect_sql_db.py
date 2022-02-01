import psycopg2
import os

def creat_db():
    #establishing the connection
    try:
        conn = psycopg2.connect(database='ALIMCONFIANCE', user='postgres', password='password')
    except psycopg2.OperationalError:
        os.system('sh scripts/creat_data_base.sh')
        conn = psycopg2.connect(database='ALIMCONFIANCE', user='postgres', password='password')

    conn.autocommit = True

    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    #Preparing query to create a database
    with open('scripts/creat_table_sql') as f:
        lines = str(("".join(f.readlines())))
        f.close()

    #Creating a database
    cursor.execute(lines)
    print("Database and tables created successfully........")

    #Closing the connection
    conn.close()

def insert_values():

    try:
        conn = psycopg2.connect(database='ALIMCONFIANCE', user='postgres', password='password')
    except psycopg2.OperationalError:
        print("ERROR..........")
        return

    cursor = conn.cursor()

    #read the script that insert into data base
    with open('CSV_ETABLISSEMENT.csv') as f:
        cursor.copy_from(f, 'etablissement', sep=',')
        cursor.execute('ALTER TABLE ETABLISSEMENT DROP COLUMN erro1')
        conn.commit()
        f.close()


    with open('CSV_INSPECTION.csv') as f:
        cursor.copy_from(f, 'inspection', sep=',')
        cursor.execute('ALTER TABLE INSPECTION DROP COLUMN erro1')
        conn.commit()
        f.close()

    print("Data unsertion OK........")
    os.remove("CSV_INSPECTION.csv")
    os.remove("CSV_ETABLISSEMENT.csv")
    print("2 CSV_DELETED......")


