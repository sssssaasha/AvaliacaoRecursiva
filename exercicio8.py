#Escreva o corpo da função recursiva para computar S(n) para uma dada seqüência S(1 ponto):
#a) 1 , 3 , 9 , 27 , ...
#1 1
#b) 2 , 1 , 2 , 4 , ...
#c) a , b , a + b , a + 2b , 2a + 3b , ...
#d) p , p – q , p + q , p – 2q , p + 2q , p – 3q , ...

def s(n, sequencia_tipo):
  if n == 0:
      return 0

  if sequencia_tipo== 'a':
      return pow(3, n-1)
  elif sequencia_tipo == 'b':
      if n == 1:
          return 2
      elif n == 2:
          return 1
      else:
          return s(n-1, 'b') + s(n-2, 'b')
  elif sequencia_tipo == 'c':
      if n == 1:
          return 'a'
      elif n == 2:
          return 'b'
      else:
          return s(n-1, 'c') + s(n-2, 'c')
  elif sequencia_tipo == 'd':
      p = 10
      q = 4
      if n % 2 == 0:
          return p + ((n//2) - 1) * q
      else:
          return p - (n//2) * q

# TESTANDO A FUNÇÃO
sequencia = 'd'
for n in range(1, 8):
  resultado = s(n, sequencia)
  print(resultado)
