import copy

lis1 = [3,4,5,2,4,56,5]

lis2 = lis1[:]
print "Slicing",lis2

clonninglist = []
clonninglist.extend(lis1)
print "Clonning List",clonninglist

li = list(lis1)
print "Simple list",li

shallowcopy = copy.copy(lis1)
print "shallow copy",shallowcopy
print hex(id(shallowcopy))
print hex(id(lis1))