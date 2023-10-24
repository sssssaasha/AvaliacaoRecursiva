# 2 Escreva uma definição recursiva para uma progressão geométrica com termo inicial a e razão r.

def progressao_geometrica(a, r):
    if a == 0:
        return 0
    elif r == 1:
        return a
    else:
        return a + progressao_geometrica(a * r, r)
