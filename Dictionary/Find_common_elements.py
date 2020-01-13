from collections import Counter
ar1 = [1, 5, 10, 20, 40, 80,80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
resultdict = dict(Counter(ar1) & Counter(ar2) & Counter(ar3))
print resultdict.keys()
print resultdict
print Counter(ar1)