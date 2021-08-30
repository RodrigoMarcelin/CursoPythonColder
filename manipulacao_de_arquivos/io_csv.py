import csv

with open(r'C:\Users\Rodrigo\Documents\Documentos do Rodrigo\cursos\CursoPythonColder\manipulacao_de_arquivos\pessoas.csv') as entrada:
    for pessoa in csv.reader(entrada):
        print('Nome: {}, Idade: {}'.format(*pessoa))