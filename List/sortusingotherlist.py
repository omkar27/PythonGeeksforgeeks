list1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
list2 = [ 0,   1,   1,    0,   1,   2,   2,   0,   1]
c = zip(list1,list2)
print zip(list1,list2)
print [x for _, x in sorted(c)]
print list(sorted(c))