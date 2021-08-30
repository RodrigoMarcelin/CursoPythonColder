# [expressão for item in list is condicional]
dobros = [i * 2 for i in range(100000)]
print(dobros)

# Versão "normal"
dobros = []
for i in range(100000):
    dobros.append(i * 2)
print(dobros)