def rem(a,i):
    print a
    b = ""
    for an in range(len(a)):
        if an != i:
            b = b+a[an]
    print "Str",b
    print [a[j] for j in range(len(a)) if j != i]
    print list(filter(lambda x: x!=i,a))
b = "Omkar"
rem(b,2)

