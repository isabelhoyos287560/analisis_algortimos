import random
import time
import matplotlib.pyplot as plt
import seaborn as sns


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def merge_sort(arr):
    # Caso base
    if len(arr) <= 1:
        return arr

    # Dividir
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    # Combinar
    return merge(left, right)


def insertion_sort(arr):
    resultado = arr.copy()

    for i in range(1, len(resultado)):
        key = resultado[i]
        j = i - 1

        while j >= 0 and resultado[j] > key:
            resultado[j + 1] = resultado[j]
            j = j - 1

        resultado[j + 1] = key

    return resultado


def medir_tiempo_ordenamiento(n):
    arr = [random.randint(0, 10000) for _ in range(n)]
    arr1 = arr.copy()

    inicio_t1 = time.time()
    resultado_merge = merge_sort(arr)
    fin_t1 = time.time()

    inicio_t2 = time.time()
    resultado_insertion = insertion_sort(arr1)
    fin_t2 = time.time()

    print(f"n = {n}")
    print(f"Tiempo merge sort: {fin_t1 - inicio_t1:.6f} segundos")
    print(f"Tiempo insertion sort: {fin_t2 - inicio_t2:.6f} segundos")
    print(f"Primeros elementos merge sort: {resultado_merge[:10]}")
    print(f"Primeros elementos insertion sort: {resultado_insertion[:10]}")
    print("-" * 50)

    return fin_t1 - inicio_t1, fin_t2 - inicio_t2


if __name__ == "__main__":
    tiempos_merge = []
    tiempos_insertion = []

    datos = [10, 50, 100, 500, 1000, 5000]

    for n in datos:
        tiempo_merge, tiempo_insertion = medir_tiempo_ordenamiento(n)
        tiempos_merge.append(tiempo_merge)
        tiempos_insertion.append(tiempo_insertion)

    sns.lineplot(x=datos, y=tiempos_merge, label="Merge Sort")
    sns.lineplot(x=datos, y=tiempos_insertion, label="Insertion Sort")

    plt.xlabel("Cantidad de datos (N)")
    plt.ylabel("Tiempo de ejecucion (s)")
    plt.title("Comparacion entre Merge Sort e Insertion Sort")
    plt.grid()
    plt.show()