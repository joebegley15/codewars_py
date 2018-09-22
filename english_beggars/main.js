def beggars(values, n):
    arr = []
    for i in range(0,n):
        arr.append(0)
    if n != 0:
        for i in range(0,len(values)):
            arr[i%n] += values[i]
    return arr