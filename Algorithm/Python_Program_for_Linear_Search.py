
def lin(a,x):

    for i in range(len(a)):
        if x == a[i]:
            return i
    return -1
a = [43, 5, 34, 23, 4, 5]
x = 4
print lin(a,x)