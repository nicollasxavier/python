nome=str(input('Digite seu nome completo: ')).strip()
print('Analisando seu nome...')
maiusculo=nome.upper()
print('Seu nome em maiúsculas é {}'.format(maiusculo))
minusculo=nome.lower()
print('Seu nome em minúsculo é {}'.format(minusculo))
cont=len(nome) - nome.count(' ')
print('Seu nome tem ao todo {} letras'.format(cont))

pname=nome.split()
pnametotal=pname[0]
contl=len(pnametotal)
print('Seu primeiro nome é {} e ele tem {} letras'.format(pnametotal, contl))