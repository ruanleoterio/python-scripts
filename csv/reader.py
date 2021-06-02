import csv


def read_csv(filename='database.csv'):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_reader.__next__()

        client = []
        for row in csv_reader:
            dicio = {"nome": row[0], "domínio": row[1]}
            client.append(dicio)

        print(client)


if __name__ == '__main__':
    read_csv()
