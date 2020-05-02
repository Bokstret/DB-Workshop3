import cx_Oracle
import re
import csv

username = 'Boks'
password = 'BOKS'
database = 'localhost' 
connection = cx_Oracle.connect(username,password, database)
cursor = connection.cursor()

filename = "projects.csv"

with open(filename, newline='') as file:
    reader = csv.DictReader(file)
    tables = ['Collection','Project','ProjectCountry','ProjectCategory'] 
    for i in tables:
        cursor.execute("DELETE FROM " + i)
    CategoryList = []
    CountryList = []
    
   
    try:
        for row in reader:
            
            projectid = int(row['ID'])
            title = row['name']
            country = row['country']
            category = row['category']
            
            collected = float(row['pledged'])
            goal = float(row['goal'])
            currency = row['currency']
            launched = row['launched']
            
            if country not in CountryList:
                CountryList.append(country)
                query = """INSERT INTO ProjectCountry(country) VALUES (:country)"""
                cursor.execute(query, country=country)
                

            if category not in CategoryList:
                CategoryList.append(category)
                query = """INSERT INTO ProjectCategory(main_category) VALUES (:category)"""
                cursor.execute(query, category=category)

     
            query = """INSERT INTO Project(projectid,title,country,main_category) VALUES (:projectid,:title,:country,:main_category)"""
            cursor.execute(query, projectid = projectid, title=title, country = country, main_category = category)	

            query = """INSERT INTO Collection(projectid,collected,goal,currency,launched) VALUES (:projectid,:collected,:goal,:currency,TO_DATE(:launched,'RR.MM.DD HH24:MI:SS'))"""
            cursor.execute(query, projectid = projectid, collected=collected, goal = goal, currency = currency,launched = launched)	

            
  

          
    except:
        
        raise
    
    finally:
        
        connection.commit()   
        cursor.close()
        connection.close()
