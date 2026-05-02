n = int(input('Digite um numer entre 0 e 9999: '))
n1 = str(n)
print(f'Unidade: {n1[3]}')
print(f'Dezena:  {n1[2]}')
print(f'Centena: {n1[1]}')
print(f'Milhar:  {n1[0]}')

#ou

num = int(input('Digite um numero entre 0 e 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')
