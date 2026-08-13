from math import hypot
opo=float(input('Comprimento do cateto oposto: '))
adj=float(input('Comprimento do cateto adjacente: '))
hip= hypot(opo, adj)
print('A hipotenusa vai medir {:.2f}'.format(hip))