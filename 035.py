print('Vamos calcular se é possivel formar um triangulo!')
t1 = float(input('Primeira reta: '))
t2 = float(input('Segunda reta: '))
t3 = float(input('Terceira reta: '))

if t1 + t2 > t3 and t2 + t3 > t1 and t1 + t3 > t2:
    print('Pode formar um triangulo')
else: print('NÃo pode formar um triangulo')
