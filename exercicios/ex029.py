v=float(input('Qual é a velocidade atual do carro? '))
total= (v-80)
final=total*7
if v > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h \nVocê deve pagar uma multa de R${:.2f}! \nTenha um bom dia! Dirija com segurança!'.format(final))
else:
    print('Tenha um bom dia! Dirija com segurança!')