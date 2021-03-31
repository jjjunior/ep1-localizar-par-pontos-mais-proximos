"""
Ipt - Instituto de Pesquisas Tecnológicas
Professor: Prof. Dr. Eng. Eduardo Takeo Ueda

Curso: Mestrado Profissional em Computação Aplicada
Disciplina: Estrutura de Dados e Análise de Algoritmos

Aluno: João José Maranhão Junior
Período: Primeiro Quadrimestre
"""

# Algoritmo de divisao em conquista feito em Python3
# que encontra a menor distancia dado um conjunto de
# pontos P.
import math

from par_de_pontos_util import copia_array
from quick_sort import QuickSort


# Calcula a distancia euclidiana dado 2 pontos
# Entrada: Um par de pontos p1 e p2
def distancia(p1, p2):
    return math.sqrt((p1.x - p2.x) * (p1.x - p2.x) +
                     (p1.y - p2.y) * (p1.y - p2.y))


# Retorna menor distancia entre dois pontos
# Entrada:
#       - P: Array que representa um conjuntos de pontos
#       - n: Tamanho do conjunto
def procura_menor_distancia(P, n):
    menor_distancia = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            if distancia(P[i], P[j]) < menor_distancia:
                menor_distancia = round(distancia(P[i], P[j]), 2)
    print("\tMenor distancia:", menor_distancia)
    return menor_distancia


# Funcão que procura a menor distancia entre os pontos mais proximos,
# dado um conjuntos de pontos de tamanho n. Todos os pontos
# do conjuntos é ordenado baseado na coordenada y e sao limitados
# na distancia minima d.
# Esta função parece ser O(n^ 2), mas é O(n), pois a função é
# executada no máximo 6 vezes.
def faixa_pontos_proximos(pontos, tamanho, d):
    # Inicializando a menor distancia
    menor_distancia = d


    # Pega todos os pontos um a um até que a diferença
    # entre as coodenadas y seja menor que d
    # Este fato comprova que este loop itera no maximo 6 vezes.
    for i in range(tamanho):
        j = i + 1
        while j < tamanho and (pontos[j].y - pontos[i].y) < menor_distancia:
            menor_distancia = round(distancia(pontos[i], pontos[j]), 4)
            j += 1

    return menor_distancia

# Funçao recursiva que localiza a menor ponto.
def localiza_pontos(P, Q, n):
    # Se houver até 3 pontos retorna menor_distancia
    if n <= 3:
        return procura_menor_distancia(P, n)

    # Calculando meio com teto
    meio = n // 2
    ponto_medio = P[meio]

    pl = localiza_pontos(P[:meio], Q, meio)
    pr = localiza_pontos(P[meio:], Q, n - meio)

    # Encontra a menor entre as duas distancias
    d = min(pl, pr)

    # Constroi um array que contem os pontos mais proximos de d
    # passando o ponto medio.
    pontos_proximos = []
    for i in range(n):
        if abs(Q[i].x - ponto_medio.x) < d:
            pontos_proximos.append(Q[i])

    # Procurando o ponto mais proximo dado um faixa de pontos
    # Returna o minimo mais proximo
    return min(d, faixa_pontos_proximos(pontos_proximos, len(pontos_proximos), d))


# Funcão que encontra a menor distancia
def menor_distancia(P):
    n = len(P)

    print("\tConjunto de pontos P desordenados", P)
    quick = QuickSort()
    quick.sort(P, lambda p1, p2: p1.x > p2.x)
    print("\tConjunto de pontos P ordenados em x", P)

    Q = copia_array(P)

    quick.sort(Q, lambda p1, p2: p1.y > p2.y)
    print("\tConjunto de pontos Q ordenados em y", Q)

    return localiza_pontos(P, Q, n)
