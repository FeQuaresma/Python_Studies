arr = [52, 21, 13, 33, 82, 68, 76]
ordenado = []
count = 0

# 1) ordernar o array (crescentemente) usando for

'''for n in arr:
    if ordenado == [] or ordenado[-1] < n:
        ordenado.append(n)
    else:
        for c in ordenado:
            if c > n:
                ordenado.insert(ordenado.index(c), n)
                break'''

# 2) ordernar o array (crescentemente) usando while

while count < len(arr):
    if ordenado == [] or ordenado[-1] <= arr[count]:
        ordenado.append(arr[count])
    else: 
        subcounter = 0
        while subcounter < len(ordenado):
            if arr[count] < ordenado[subcounter]:
                ordenado.insert(ordenado.index(ordenado[subcounter]), arr[count])
                break
            subcounter += 1

    count += 1

# 3) ordernar o array (crescentemente) sem usar loop (usando métodos nativos)

'''arr.sort()'''


print(arr)
print(ordenado)