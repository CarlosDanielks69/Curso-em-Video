n = int(input('Digite um numero: '))
d = n * 2
t = n * 3
r = pow(n, 1/2)
print(f'O dobro do numero {n} é: {d}')
print(f'O triplo do numero {n} é: {t}')
print(f'A raiz quadrada do numero {n} é: {r:.3f}')

#ou


n1 = int(input('Digite um numero: '))
print(f'O dodro de {n1} é: {n1*2}. \nO Triplo do numero \
{n1} é {n1*3}. \nA raiz quadrada do numero {n1} é {pow(n1,1/2):.3f}')
