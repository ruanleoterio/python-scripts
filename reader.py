import csv

with open('database.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    csv_reader.__next__()
    client = []
    for row in csv_reader:
        dicio = {"nome": row[0], "domínio": row[1]}

        client.append(dicio)
    print(client)

