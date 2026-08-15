salario=float(input('Qual é o salário do funcionário? R$'))

p1=(salario*10)/100
p1final=salario+p1
p2=(salario*15)/100
p2final=salario+p2

if salario > 1250:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, p1final))
if salario <= 1250:
    print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, p2final))