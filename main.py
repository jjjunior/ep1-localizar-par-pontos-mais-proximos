from par_de_pontos import menor_distancia
from par_de_pontos_util import ler_arquivo, limpa_terminal
from ponto import Ponto


def cabecalho(nlinhas):
    print("***" * nlinhas)
    print('''
    Ipt - Instituto de Pesquisas Tecnológicas
    Professor: Prof. Dr. Eng. Eduardo Takeo Ueda

    Curso: Mestrado Profissional em Computação Aplicada
    Disciplina: Estrutura de Dados e Análise de Algoritmos

    Aluno: João José Maranhão Junior
    Período: Primeiro Quadrimestre

    Exercicio Programa: Algoritmo de divisao e conquista feito em Python3
    que encontra a menor distancia dado um conjunto de pontos P em O(n log n)
    ''')
    print("***" * nlinhas)


def menu():
    nlinhas = 50
    limpa_terminal()
    cabecalho(nlinhas)
    opcao = 0
    while opcao != 3:
        print('''\n\t[1] - Fazer input dos pontos manualmente\n\t[2] - Fazer input via arquivo\n\t[3] - Sair\n''')
        opcao = int(input("\tQual é a sua opção?"))
        if opcao == 1:
            opcao_pontos = "s"
            P = []
            while opcao_pontos == "s":
                x = float(input("\tCoodenada X do ponto:"))
                y = float(input("\tCoodenada Y do ponto:"))
                P.append(Ponto(x, y))
                opcao_pontos = str(input("\tDeseja incluir mais um ponto(s/n)?"))
                while opcao_pontos != "s" and opcao_pontos != "n":
                    opcao_pontos = str(input("\tDigite s(sim) ou n(não)?"))
            if len(P) > 0:
                print("=-=" * nlinhas)
                print("\tA distancia dos pontos mais proximos é: ", menor_distancia(P))
                print("=-=" * nlinhas)
        elif opcao == 2:
            path = str(input("\tDigite o caminho absoluto do arquivo:"))
            P = ler_arquivo(path)
            print("=-=" * nlinhas)
            print("\tA distancia dos pontos mais proximos é: ", menor_distancia(P))
            print("=-=" * nlinhas)
        elif opcao == 3:
            print("\tFinalizando programa !!")
        else:
            print("\tOpção inválida, Tente novamente")
        print("***" * nlinhas)


if __name__ == '__main__':
    menu()
