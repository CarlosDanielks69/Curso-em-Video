d = float(input('Alugado por quantos dias? '))
km = float(input('Quantos Km foram rodados? '))
t = (d * 60) + (km * 0.15)
print(f'O total a pagar é de R${t:.2f}')
