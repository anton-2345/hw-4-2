def nod(a, b):
    if b==0:
        return a
    else:
        return nod(b, a % b)
a = int(input('Первое число'))
b = int(input('Второе число'))
print(nod(a, b))