import random
import time

def bubble_sort(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista

# Função para testar o bubble sort com diferentes tamanhos
def testar_bubble_sort(tamanho):
    lista = [random.randint(0, 1000) for _ in range(tamanho)]  # cria lista aleatória
    print(f"\nLista original ({tamanho} elementos):")
    print(lista)

    inicio = time.time()
    lista_ordenada = bubble_sort(lista)
    fim = time.time()

    print(f"Lista ordenada ({tamanho} elementos):")
    print(lista_ordenada)
    print(f"Tempo de execução: {fim - inicio:.4f} segundos")

# Testes com diferentes tamanhos 10, 100, 1000 de vetor
testar_bubble_sort(10)
testar_bubble_sort(100)
testar_bubble_sort(1000)
