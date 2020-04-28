import cx_Oracle
import chart_studio
import re
chart_studio.tools.set_credentials_file(username='Bokstret', api_key='hlqtm5SJaSFu9KeNwNWC')
import plotly.graph_objects as go
import chart_studio.plotly as py
import chart_studio.dashboard_objs as dash
username = 'Boks'
password = 'BOKS'
database = 'localhost' 
connection = cx_Oracle.connect(username,password, database)
cursor = connection.cursor()

def GetId(url):
    name = re.findall("~[A-z.]+/[0-9]+", url)[0][1:]
    return name.replace('/', ':')
   	

#Запрос 1
print("Запрос 1: Количество выпущенных проектов в каждой стране.\n")
names = []
Bvalues = []
query = """
SELECT
    country,
    COUNT(*) AS amount
FROM
    project_collection
GROUP BY
    country
"""
cursor.execute(query) 


for row in cursor.fetchall():
    names.append (row[0])
    Bvalues.append(row[1]) 
bar = go.Bar (x = names, y = Bvalues)
bar = py.plot([bar],auto_open = True, file_name = "Plot1")

#Запрос 2
print("\nЗапрос 2: Количество проектов по странам в %.\n")
labels = []
Pvalues = []
query = """
SELECT
    country,
    round(COUNT(*) * 100 / t1.total, 1) AS persent
FROM
    project_collection,
    (
        SELECT
            COUNT(*) total
        FROM
            project_collection
    ) t1
GROUP BY
    country,
    t1.total
"""
cursor.execute(query)

for row in cursor.fetchall():
    labels.append (row[0])
    Pvalues.append(row[1]) 
pie = go.Pie (labels = labels, values = Pvalues)
pie = py.plot([pie],auto_open = True, file_name = "Plot2",)

#Запрос 3
print("\nЗапрос 3: Выпуск проектов по годам.\n")
years = []
Tvalues = []
query = """
SELECT
    EXTRACT(YEAR FROM launched) AS year,
    COUNT(*) AS amount
FROM
    project_collection
GROUP BY
    EXTRACT(YEAR FROM launched)
ORDER BY
    EXTRACT(YEAR FROM launched)
"""
cursor.execute(query) 
for row in cursor.fetchall():
    years.append (row[0])
    Tvalues.append(row[1]) 
scatter = go.Scatter (x = years, y = Tvalues)
scatter = py.plot([scatter],auto_open = True, file_name = "Plot3")


my_dash = dash.Dashboard()
bar_id = GetId(bar)
pie_id = GetId(pie)
scatter_id = GetId(scatter)
box_1= {
    'type': 'box',
    'boxType': 'plot',
    'fileId': bar_id,
    'title': 'Запрос 1: Количество выпущенных проектов в каждой стране.'
}

box_2 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': pie_id,
    'title': 'Запрос 2: Количество проектов по странам в %.'

}

box_3 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId': scatter_id,
    'title': 'Запрос 3: Выпуск проектов по годам.'
}


my_dash.insert(box_1)
my_dash.insert(box_2, 'below', 1)
my_dash.insert(box_3, 'right', 2)

py.dashboard_ops.upload(my_dash, 'Workshop3')

cursor.close()
connection.close()