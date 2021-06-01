import csv


def client():
    with open('database.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_reader.__next__()

        clientes = []
        for row in csv_reader:
            dicio = {"nome": row[0], "domínio": row[1]}
            clientes.append(dicio)
        print(clientes)
client()