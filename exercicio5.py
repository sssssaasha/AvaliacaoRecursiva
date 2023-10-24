# 5 Uma coleção S de cadeias de caracteres é definida recursivamente por:
#a E S e b E S
#Se X E S, então Xb E S.
#Quais das seguintes cadeias pertencem a S? a , ab , aba , aaab , bbbbb
#Faça um programa recursivo para demonstrar. 

def haha(s):
  if s == "":
    return True
  elif s[0] == 'a' and haha(s[1:]):
    return True
  elif s[-1] == 'b' and haha(s[:-1]):
    return True
  else:
    return False

strings = ["a", "ab", "aba", "aaab", "bbbbb"]

for string in strings:
  if haha(string):
      print(f"{string} pertence a S")
