#Membros antigos da Sociedade de Pitágoras definiram números figurados como sendo o
#número de pontos em uma certa configuração geométrica. Os primeiros números #triangulares
#são 1, 3, 6 e 10
#Encontre a fórmula para o n-ésimo número triangular e escreva um programa recursivo

def numero_triangular(n):
  if n == 1:
    return 1
  else:
    return n + numero_triangular(n-1)

n = 4
resultado = numero_triangular(n)
print(resultado)
