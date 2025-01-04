import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

#try:
#    with open(ROOT_PATH / 'usuarios.csv', 'w', encoding='utf-8') as arquivo:
#        escritor = csv.writer(arquivo)
#        escritor.writerow(['id', 'nome'])
#        escritor.writerow(['1', 'Maria'])
#        escritor.writerow(['2', 'João'])
#except IOError as exc:
#    print(f"Erro ao criar o arquivo. {exc}")


try:
    with open(ROOT_PATH / 'usuarios.csv', 'r', newline='utf-8') as csvfile:
        leitor = csv.reader(csvfile)
        for row in leitor:
            print(row['first_name'], row['last_name'])
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")