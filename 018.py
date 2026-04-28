from math import radians, sin, cos, tan
angulo = float(input('Digite o angulo que deseja: '))
seno = sin(radians(angulo))
print(f'O angulo de {angulo} tem o SENO de {seno:.2f}')
cosseno = cos(radians(angulo))
print(f'O angulo de {angulo} tem o COSSENO de {cosseno:.2f}')
tangente = tan(radians(angulo))
print(f'O angulo de {angulo} tem a TANGENTE de {tangente:.2f}')
