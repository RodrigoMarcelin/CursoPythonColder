with open(r'C:\Users\Rodrigo\Documents\Documentos do Rodrigo\cursos\CursoPythonColder\manipulacao_de_arquivos\pessoas.csv') as arquivo:
    

    for registro in arquivo:
        print('Nome: {}, Idade: {}'.format(*registro.strip().split(',')))

if arquivo.closed:
    print('Arquivo fechado')
