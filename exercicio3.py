# 3 Uma coleção T de números é definida recursivamente por:
#2 E T
#Se X E T, então X+3 E T e 2*X E T
#Quais dos seguintes números pertencem a T? 6 , 7 , 19 , 12.
#Faça um programa recursivo para demonstrar

def pertence_a_T(n):
  if n == 2:
    return True
  if n < 2:
    return False
  if pertence_a_T(n - 3) or pertence_a_T(n // 2):
    return True
  return False

numeros = [6, 7, 19, 12]
for numero in numeros:
  if pertence_a_T(numero):
    print(f"{numero} pertence a T")
  else:
    print(f"{numero} não pertence a T")
