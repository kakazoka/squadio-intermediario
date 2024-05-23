valor = float(input())

if valor > 0:
  print('Depósito realizado com sucesso!')
  print(f'Saldo atual: R$ {valor:.2f}')
elif valor < 0:
  print('Valor inválido! Digite um valor maior do que zero.')
else:
  print('Operação encerrada.')
