# 6 Uma coleção W de cadeias de símbolos é definida recursivamente por:
# a pertence a W, b pertence a W e c pertence a W
# Se X pertence a W, então a(X)c pertence a W.
# Quais das seguintes cadeias pertencem a S? a(b)c , a(a(b)c)c , a(abc)c , a(a(a(a)c)c)c, a(aacc)c
# Faça um programa recursivo para demonstrar

def W(string):
  if string == "":
    return True
  elif len(string) >= 3 and string[0] == "a" and string[-1] == "c":
    return W(string[1:-1])
  else:
    return False

strings = ["a(b)c", "a(a(b)c)c", "a(abc)c", "a(a(a(a)c)c)c", "a(aacc)c"]

for string in strings:
  if W(string):
    print(f"{string} pertence ao W")
  else:
    print(f"{string} não pertence ao W")
