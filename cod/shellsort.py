def shellSort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

# Lista de números inteiros para ordenar
arr = [64, 25, 12, 22, 11, 90, 50, 45, 34, 76, 87, 65, 21, 33, 56]

print("Lista antes da ordenação:")
print(arr)

shellSort(arr)

print("Lista após a ordenação:")
print(arr)