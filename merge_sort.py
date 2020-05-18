def mergesort(n):

    if len(n) > 1:

        mid = len(n)//2
        left = n[:mid]
        right = n[mid:]
        mergesort(left)
        mergesort(right)
        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                n[k] = left[i]
                i += 1
            else:
                n[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            n[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            n[k] = right[j]
            j += 1
            k += 1

        return n

n = [100, 50, 10, 60, 20, 80, 90]
m = mergesort(n)
print(m)