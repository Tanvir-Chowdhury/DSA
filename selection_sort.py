def selectionSort(n):
    for i in range(0, len(n)-1):
        index_min = i
        for j in range(i, len(n)):
            if n[j] < n[index_min]:
                index_min = j

        if index_min != i:
            n[i], n[index_min] = n[index_min], n[i]

    return n


print(selectionSort([12, 36, 902, 5, 25]))
