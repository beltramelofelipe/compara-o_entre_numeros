num = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if(num > num2):
  print('O numéro {} é maior que o número {}'.format(num, num2))
elif(num2 > num):
  print('O numéro {} é maior que o número {}'.format(num2, num))
else:
  print('Os numeros são iguais')
