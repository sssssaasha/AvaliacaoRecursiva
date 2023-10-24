#Considere o algoritmo recursivo:
#Lista Rotina (Lista L, inteiro j) {
#Se (j == 1)
#return L;
#Encontre o L[i], o maior item da lista L entre 1 e j;
#Troque o L[i] pelo item L[j];
#return Rotina (L, j – 1);
#}
#Para L = [3, 7, 4, 2, 6 ] faça a chamada Rotina (L, 5);:
#a) Represente L e o total de chamadas realizadas à Rotina
def Rotina(L, j):
  if j == 1:
      return L
  i = L.index(max(L[:j]))
  L[i], L[j-1] = L[j-1], L[i]
  return Rotina(L, j-1)

L = [3, 7, 4, 2, 6]
resultado = Rotina(L, 5)
total_chamadas = 5

print("L:", L)
print("Chamadas Totais:", total_chamadas)
print("Resultado:", resultado)
