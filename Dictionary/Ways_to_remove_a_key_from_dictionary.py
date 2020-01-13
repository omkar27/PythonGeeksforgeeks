a = {}
a["a"] = "Omkar"
a["b"] = "baba"
a["c"] = "Jordan"
del a["a"]
print a.pop("b")
print a

b = {}
b[1] = "One"
b[2] = "Two"
b[3] = "Three"
b[4] = "Four"
print b.items()
c = {key:val for key,val in b.items() if key != 1}
print {key:val for key,val in b.items() if key != 1}

print "the new directory after removal is {}".format(c)