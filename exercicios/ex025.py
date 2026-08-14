#Programa que verifica se o nome da pessoa tem silva
nome=str(input('Qual é seu nome completo? ')).strip()

print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))