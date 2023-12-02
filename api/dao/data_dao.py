import csv
import os


class CSVDAO:
    @staticmethod
    def ler_csv():
        file_csv = os.path.abspath(r'api/source/database/database.csv')
        with open(file_csv, newline='', encoding='utf-8'
                  ) as arquivo_csv:
            leitor = csv.DictReader(arquivo_csv)
            dados = [linha for linha in leitor]

        return dados
