"""
Ipt - Instituto de Pesquisas Tecnológicas
Professor: Prof. Dr. Eng. Eduardo Takeo Ueda

Curso: Mestrado Profissional em Computação Aplicada
Disciplina: Estrutura de Dados e Análise de Algoritmos

Aluno: João José Maranhão Junior

Exercicio: Localizar a distancia entre o par de pontos mais proximos

"""

#Classe responsável por armazenas as coordenadas cartesianas do ponto
class Ponto:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    def __repr__(self):
        return "(x:%s y:%s)" % (self._x, self._y)