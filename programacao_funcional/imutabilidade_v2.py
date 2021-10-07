from locale import setlocale, LC_ALL
from calendar import mdays, month_name
from functools import reduce

# Português do Brasil
setlocale(LC_ALL, 'pt_BR')

# Listar todos os meses do do ano com 31 dias
# 1. (filter) pegar os indices de todos os meses com 31 dias 1, 3, 5...
# 2. (map) transformar os índices em nome
# 3. (reduce) jundar tudo para imprimir

def mes_com_31(mes):
    return mdays[mes] == 31

def get_nome_mes(mes):
    return month_name[mes]

def juntar_meses(todos, nome_mes):
    return f'{todos}\n- {nome_mes}'


print(reduce(juntar_meses, map(get_nome_mes, filter(mes_com_31, range(1,13))), 'Meses com 31 dias:'))