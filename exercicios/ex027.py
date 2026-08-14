nome=str(input('Digite seu nome completo: ')).strip()

form=nome.split()
formi=form[0]
formf=form[-1]
print('Prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(formi))
print('Seu último nome é {}'.format(formf))