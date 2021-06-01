import csv

with open('database.csv', 'a', newline='') as file:
    writer = csv.writer(file)
    name = input("nome:")
    domain = input("domínio:")
    have_name = bool(nome)
    have_domain = bool(dominio)

    writer.writerow([name, domain, "", have_name, have_domain])

