d = float(input('Alugado por quantos dias? '))
km = float(input('Quantos Km foram rodados? '))
cd = d * 60
Kmr = km * 0.15
t = cd + Kmr
print(f'O total a pagar é de R${t:.2f}')
