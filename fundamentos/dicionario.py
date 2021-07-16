pessoa = {'nome': 'Prof. Ana', 'idade': 38, 'cursos': ['inglês', 'Português']}

print(len(pessoa))

print(pessoa.keys())
print(pessoa.values())
print(pessoa.items())
print(pessoa.get('nome'))
print(pessoa.get('tags', []))

pessoa['idade'] = 48
print(pessoa)
pessoa['cursos'].append('Angular')
print(pessoa)
pessoa.pop('idade')
print(pessoa)
pessoa.update({'idade': 40, 'Sexo': 'M'})
print(pessoa)
del pessoa['cursos']
print(pessoa)
pessoa.clear()
print(pessoa)