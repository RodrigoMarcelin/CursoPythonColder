a1 = [1, 2, 3]
a2 = []

for i in a1:
    a2.append(i * 2)

print(a2)

m = map(lambda i: i * 2, a1)

print(list(m))

mt = tuple(map(lambda i: i ** 2, a1))

print(mt)