# 4 Uma coleção M de números é definida recursivamente por:
# 2 pertence a M e 3 pertence a M
# Se X pertence a M e Y pertence a M, então X*Y pertence a M .
# Quais dos seguintes números pertencem a M? 6 , 9 , 16 , 21 , 26 , 54 , 72 , 218.
# Faça um programa recursivo para demonstrar.


def pertence_a_M(n):
  if n == 2 or n == 3:
      return True
  elif n < 2:
      return False
  elif n % 2 == 0:
      return pertence_a_M(n // 2)
  elif n % 3 == 0:
      return pertence_a_M(n // 3)
  else:
      return False

numeros = [6, 9, 16, 21, 26, 54, 72, 218]

for numero in numeros:
  if pertence_a_M(numero):
      print(f'{numero} pertence a M')
  else:
      print(f'{numero} não pertence a M')
