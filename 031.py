n = float(input('Qual a distancia? '))
if n < 200:
    d = n * 0.5
    print(f'O preço da viagem será de {d}')
else:
    d = n * 0.45
    print(f'O preço da viagem será de {d}')
