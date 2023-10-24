# Alex Menegatti Secco
# Anna Bosquilia Navarro
# Mariana de Castro
# Tarso Bertolini Rodrigues
# Grupo 30

# 1. Escreva um algoritmo recursivo para cada uma das alternativas

# a) 
# S(1) = 10
# S(n) = S(n – 1) + 10, para n >= 2
def s(n):
  if n == 1:
    return 10

  else:
    return s(n-1) + 10

print(f'Letra a: {s(3)}')
    

#B
#A(1) = 2
#A(n) = A(n – 1)**-1 , para n >= 2

def A(n):
    if n == 1:
        return 2
    else:
        return A(n-1)**-1

print(f'Letra b: {A(3)}')


# c)
#B(1) = 1
#B(n) = B(n – 1) + n2, para n >= 2

def b(n):
  if n == 1:
    return 1
    
  else:
    return b(n-1) + n**2

print(f'Letra c: {b(5)}')


# d)
#P(1) = 1
#P(n) = n2*P(n – 1) + n - 1, para n >= 2

def P(n):
    if n == 1:
        return 1
    else:
        return n**2 * P(n-1) + n - 1

print(f'Letra d: {P(5)}')

# e)
# D(1) = 3
# D(2) = 5
# D(n) = (n – 1)*D(n – 1) + (n – 2)*D(n – 2), para n > 2
def d(n):
  if n == 1:
    return 3
  elif n == 2:
    return 5
  else:
    return (n - 1)*d(n - 1) + (n - 2)*d(n - 2)

print(f'Letra e: {d(5)}')

# f)
#W(1) = 2
#W(2) = 5
#W(n) = W(n – 1)*W(n – 2), para n > 2

def w(n):
  if n == 1:
    return 2
  elif n == 2:
    return 5
  else:
    return w(n-1)*w(n-2)

print(f'Letra f: {w(5)}')

# g)
#T(1) = 1
#T(2) = 2
#T(3) = 3
#T(n) = T(n – 1) + 2*T(n – 2) + 3*T(n – 3), para n > 3

def t(n):
  if n == 1:
    return 1
  elif n == 2:
    return 2
  elif n == 3:
    return 3
  else:
    return t(n-1) + 2 * t(n-2) + 3 * t(n-3)

print(f'Letra g: {t(10)}')
