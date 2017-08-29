
# Yuan Zhan 26693267

# Q1
# O(n(logn)^2)


# Q2
def mergeSort(list):
    print("Splitting:", list)
    if (len(list) > 1):
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]
        print("Current left:", left)
        print("Current right:", right)

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                print("Adding left:", left[i])
                list[k] = left[i]
                i = i + 1
            else:
                print("Adding right:", right[j])
                list[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            print("right empty, Adding left:", left[i])
            list[k] = left[i]
            i = i + 1
            k = k + 1

        while j < len(right):
            print("left empty, Adding right:", right[j])
            list[k] = right[j]
            j = j + 1
            k = k + 1

    print("Merge:", list)

mergeSort([24, 13, 26, 1, 2, 27, 38, 15])