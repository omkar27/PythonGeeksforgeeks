a = [2,34,5,6,7,1,2,45,6,7]

#print list(reversed(a))

def returnlist():
    return [x for x in reversed(a)]
print returnlist()

def slicearray():
    print a[::-1]

slicearray()