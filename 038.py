n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))

if n1 > n2:
    print(f'O numero {n1} é o maior e o {n2} é o menor')
elif n2 > n1:
    print(f'O numero {n2} é o maior e o {n1} é o menor')
else: print('Não existe valor maior, os dois são IGUAIS')
