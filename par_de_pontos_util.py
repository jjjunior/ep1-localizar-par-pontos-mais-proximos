"""
Ipt - Instituto de Pesquisas Tecnológicas
Professor: Prof. Dr. Eng. Eduardo Takeo Ueda

Curso: Mestrado Profissional em Computação Aplicada
Disciplina: Estrutura de Dados e Análise de Algoritmos

Aluno: João José Maranhão Junior
Período: Primeiro Quadrimestre
"""
import platform
import subprocess

from ponto import Ponto


def copia_array(array):
    array_copiado = []
    for ponto in range(0, len(array)):
        array_copiado.append(array[ponto])
    return array_copiado

def ler_arquivo(nome_arquivo):
    array = []
    arquivo = open(nome_arquivo, "r")
    for linha in arquivo:
        ponto = linha.rstrip().split(",")
        if (len(ponto) == 2):
            p = Ponto(float(ponto[0]), float(ponto[1]))
            array.append(p)
    arquivo.close()
    return array

def limpa_terminal():
    command = "cls" if platform.system().lower()=="windows" else "clear"
    return subprocess.call(command) == 0



