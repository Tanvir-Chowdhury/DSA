def pivot_place(list1, first, last):
    pivot = list1[last]
    i = first - 1
    for j in range(first, last):
        if list1[j] < pivot:
            i += 1
            list1[i], list1[j] = list1[j], list1[i]
    list1[i+1], list1[last] = list1[last], list1[i+1]
    return i+1

def quicksort(list1, first, last):
    if first < last:
        p = pivot_place(list1, 0, last)
        quicksort(list1, 0, p-1)
        quicksort(list1, p+1, last)

list1 = [56, 26, 17, 31, 44, 93]
n = len(list1)
quicksort(list1, 0, n-1)
print(list1)
    


