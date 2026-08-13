d=int(input('Quantos dias o carro foi alugado? '))
km=float(input('Quantos km rodados? '))
dtotal=d*60
kmtotal=km*0.15
total=dtotal + kmtotal
print('O total a pagar é de R${:.2f}'.format(total))