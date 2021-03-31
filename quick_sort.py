"""
Ipt - Instituto de Pesquisas Tecnológicas
Professor: Prof. Dr. Eng. Eduardo Takeo Ueda

Curso: Mestrado Profissional em Computação Aplicada
Disciplina: Estrutura de Dados e Análise de Algoritmos

Aluno: João José Maranhão Junior

Exercicio: Localizar a distancia entre o par de pontos mais proximos

"""


# Classe responsável por ordenar um array com o algoritmos QuickSort
# o parâmetro array contendo os pontos a serem ordenados
# o parametro criterio_ordenacao escolhe um atributo da classe para
# realizar a ordenacao.
class QuickSort:

    # Método que realiza a chamado para o metodo quicksort ajustando os parametros.
    def sort(self, array, criterio_ordenacao):
        quick_sort(array, 0, len(array) - 1, criterio_ordenacao)


 #Função que realiza o particionamento baseado no PIVO
def _particiona(array, inicio, fim, criterio_ordenacao):
    pivo = array[inicio]
    min = inicio + 1
    max = fim

    while True:
        while min <= max and criterio_ordenacao(array[max], pivo):
            max = max - 1

        while min <= max and not criterio_ordenacao(array[min], pivo):
            min = min + 1

        if min <= max:
            array[min], array[max] = array[max], array[min]
        else:
            break

    array[inicio], array[max] = array[max], array[inicio]

    return max

#Funcão que realiza as chamadas recursivas apos o particionamento.
def quick_sort(array, inicio, fim, criterio_ordenacao):
    if inicio >= fim:
        return

    p = _particiona(array, inicio, fim, criterio_ordenacao)
    quick_sort(array, inicio, p - 1, criterio_ordenacao)
    quick_sort(array, p + 1, fim, criterio_ordenacao)
