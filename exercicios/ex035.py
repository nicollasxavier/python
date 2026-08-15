print('-='*15)
print('Analisador de Triângulos')
print('-='*15)
a=float(input('Primeiro segmento: '))
b=float(input('Segundo segmento: '))
c=float(input('Terceiro segmento: '))

menor1=a
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor=c

menor2=a
if b<a and b<c:
    menor=b
if c<a and c<b:
    menor=c

maior=a
if b>a and b>c:
    maior=b
if c>a and c>b:
    maior=c

soma= menor1+menor2

if soma > maior:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo!')