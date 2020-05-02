import cx_Oracle
import csv

username = 'Boks'
password = 'BOKS'
database = 'localhost' 
connection = cx_Oracle.connect(username,password, database)
cursor = connection.cursor()

tables = ['Collection','Project','ProjectCountry','ProjectCategory'] 


try:
    for i in tables:
        with open(i + '.csv', 'w', newline='') as NewFile:
            cursor.execute("SELECT * FROM " + i)
            row = cursor.fetchone()

            titles = []
            for k in cursor.description:
                titles.append(k[0])   
            print(titles)
            csv_writer = csv.writer(NewFile, delimiter=',')
            csv_writer.writerow(titles)

           
            while row:
                csv_writer.writerow(row)
                row = cursor.fetchone()

finally:
    cursor.close()
    connection.close()