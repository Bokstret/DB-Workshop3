import csv
input = open('projects.csv', 'rt')
output = open('projects2.csv', 'wt',newline='')
writer = csv.writer(output)
for row in csv.reader(input):
    
    if (len(row[7]) >= 2) or (row[8] == ''):
        writer.writerow(row)
input.close()
output.close()
