from random import randint
from time import sleep
n = randint(0, 5)
print('*'*20)
u = int(input('Vou pensar em um numero entre 0 e 5. Tente adivinhar...: '))
print('*'*20)
print('Processando...')
sleep(3)
if n == u:
    print(f'Você acertou!')
else:
    print('Você errou!')
print(f'O numero que o computador pensou foi {n}')
