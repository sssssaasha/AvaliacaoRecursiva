# 7 Forneça uma definição recursiva para todas as cadeias binárias (cadeias formadas com os
#caracteres 0 e 1) contendo um número ímpar de zeros.
def binario(n, s=''):
  if n == 0:
      if s.count('0') % 2 == 1:
          print(s)
  else:
      binario(n - 1, s + '0')
      binario(n - 1, s + '1')

n = 5
print(binario(n))
