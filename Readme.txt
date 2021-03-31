=============================================================================
    Ipt - Instituto de Pesquisas Tecnológicas
    Professor: Prof. Dr. Eng. Eduardo Takeo Ueda

    Curso: Mestrado Profissional em Computação Aplicada
    Disciplina: Estrutura de Dados e Análise de Algoritmos

    Aluno: João José Maranhão Junior
    Período: Primeiro Quadrimestre

    Exercicio Programa: Algoritmo de divisao e conquista feito em Python3
    que encontra a menor distancia dado um conjunto de pontos P em O(n log n)
===============================================================================
Pré-requisitos para execução do programa:
    - Ter instalado na maquina o python 3.8

1.0 Descompacte o arquivo ep-localizar-par-pontos-mais-proximos.zip
    - comando: unzip ep-localizar-par-pontos-mais-proximos.zip
    - entre dentro da pasta: ep-localizar-par-pontos-mais-proximos
2.0 Execução do programa
    - Digite: python3 main.py
    - Aparecerá um menu:
        [1] - Fazer input dos pontos manualmente
	    [2] - Fazer input via arquivo
	    [3] - Sair
	    - Para opção 1 - Digitar manualmente os pontos
	        Exemplo:
	            Coodenada X do ponto:1
	            Coodenada Y do ponto:2
	            Deseja incluir mais um ponto(s/n)?
	    - Para opção 2 - Input via arquivo
	        Exemplo:
	            Digite o caminho absoluto do arquivo:/Users/jotinha/pontos.txt
3.0 Formato do arquivo de entrada
    - Arquivo do tipo texto, extensão txt
    - Cada ponto em uma linha,separados por virgula, exemplo:
        10,3
        12.5,30
        40,50
        5.4,1
        -10,10.6
        3,4
        12.6,30.5
        3.6,1

Referencias para o desenvolvimento do programa:
  - CORMEN, Thomas H.. Capitulo 33 - Geometria computacional: 33.4 localizando o par de pontos mais proximo. In:CORMEN, Thomas H. et al. Algoritmos: teoria e pratica. Rio de Janeiro: Elsevier, 3. p. 757-760.
  - StackOverflow Disponível em: https://stackoverflow.com/questions/6929777/typeerror-float-object-is-not-callable. Acesso em: 13 mar. 2021.

