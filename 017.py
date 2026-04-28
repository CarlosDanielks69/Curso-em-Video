import math
cateto1 = float(input('Valor do Cateto 1: '))
cateto2 = float(input('Valor do Catero 2: '))
hipotenusa = math.hypot(cateto1, cateto2)
print(f'Hipotenusa é {hipotenusa:.2f}')
