import random
n = random.randint(1, 5)
u = int(input('Em que numero eu pensei? entre 1 e 5: '))
if n == u:
    print(f'Você acertou!')
else: print('Você errou!')
