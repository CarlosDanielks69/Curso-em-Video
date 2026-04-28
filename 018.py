import math
angulo = float(input('Ângulo: '))
radianos = math.radians(angulo)
sen = math.sin(radianos)
cos = math.cos(radianos)
tan = math.tan(radianos)
print(f'''
O seno é: {sen:.2f}
O coseno é {cos:.2f}
A tangente é {tan:.2f}''')
