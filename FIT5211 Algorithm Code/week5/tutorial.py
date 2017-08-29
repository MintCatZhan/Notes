def numOfWays(d, n):
    arr = {}
    for x in range(n + 1):
        arr[x] = 0
    arr[0] = 1
    print("initial:", arr)

    for i in range(len(d)):
        j = d[i]
        while j <= n:
            arr[j] = arr[j] + arr[j - d[i]]
            j = j + 1

    print("final: ", arr)
    return arr[n]

print(numOfWays([1,2,5], 10))