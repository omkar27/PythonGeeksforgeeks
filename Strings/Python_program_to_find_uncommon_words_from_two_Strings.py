A = "Geeks for Geeks"
B = "Learning from Geeks for Geeks"
C = ""
print A.split()
print B.split()
for i in B.split():
    if i not in A.split():
        print i,
print C
lst3 = [value for value in A.split() if value in B.split()]
#print lst3