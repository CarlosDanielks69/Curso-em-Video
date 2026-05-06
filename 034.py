s = float(input('Qual o seu salario? '))
if s >= 1250.00:
    ns = s * 0.1 + s
    a = 10
else:
    ns = s * 0.15 + s
    a = 15
print(f'''O seu salario teve um aumento de {a}%
Antigo: R${s:.2f}
Novo:   R${ns:.2f}''')
