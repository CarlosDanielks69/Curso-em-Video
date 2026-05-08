print('Simulação de emprestimo para financiamento de uma casa')
print('-'*60)
salario = float(input('Qual o seu SALARIO? '))
casa = float(input('Valor da CASA? '))
anos = float(input('Em quantos ANOS quer pagar? '))

meses = anos * 12
financiamento = casa / meses
renda = salario * 0.3
if financiamento > renda:
    print('-' * 60)
    print('Seu financiamento NÃO foi aprovado, pois a parcela exede os 30% da sua renda')
else:
    print('-' * 60)
    print('Seu financiamento foi APROVADO')

print(f'''
30% da sua renda é {renda}
Valor do Imovel: {casa}
Pacelas: {meses}
Valor Parcela: {financiamento}
''')
