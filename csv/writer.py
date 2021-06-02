import csv


def write_csv(filename='database.csv'):
    with open(filename, 'a', newline='') as file:
        writer = csv.writer(file)
        name = input("nome: ")
        domain = input("domínio: ")
        writer.writerow([name, domain, "", "TRUE", "TRUE"])


if __name__ == '__main__':
    write_csv()
