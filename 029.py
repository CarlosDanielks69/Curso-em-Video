v = float(input('Qual a velocidade do carro? '))
if v > 80:
    m = (v - 80) * 7.00
    print('Você excedeu o limite de 80km/h')
    print(f'A multa será de R${m}')
else: print('Você não excedeu o limite de velocidade.')
