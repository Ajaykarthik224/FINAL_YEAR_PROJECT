import json
import csv

with open('data.json') as json_file:
    data = json.load(json_file)

rainfall_data = data['records']

data_file = open('data_in_csv.csv', 'w')

csv_writer = csv.writer(data_file)

count = 0

for rainfall in rainfall_data:
    if count == 0:

        header = rainfall.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(rainfall.values())

data_file.close()
