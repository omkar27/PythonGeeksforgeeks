


def sel(a):
    while len(a) > 0:

        min = a[0]
        for i in range(len(a)):
            if min > a[i]:
                min = a[i]
        print min
        b.append(min)
        a.remove(min)
        sel(a)
a = [2,4,1,6,9,75,4,3]
b = []
sel(a)
print b
