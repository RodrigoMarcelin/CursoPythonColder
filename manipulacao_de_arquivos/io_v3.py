arquivo = open(r'C:\Users\Rodrigo\Documents\Documentos do Rodrigo\cursos\CursoPythonColder\manipulacao_de_arquivos\pessoas.csv')
for registro in arquivo:
    print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

arquivo.close()