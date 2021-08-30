arquivo = open(r'C:\Users\Rodrigo\Documents\Documentos do Rodrigo\cursos\CursoPythonColder\manipulacao_de_arquivos\pessoas.csv')
dados = arquivo.read()
arquivo.close()
for registro in dados.splitlines():
    print('Nome: {}, Idade: {}'.format(*registro.split(',')))