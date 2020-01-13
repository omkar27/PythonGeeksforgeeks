def uni(x):
    _size = len(x)
    repeated = []

    for i in range(_size):
        k = i+1
        for j in range(k,_size):
            if x[i] != x[j] and x[i] not in repeated:
                repeated.append(x[i])
    print repeated

a = [2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9]
uni(a)