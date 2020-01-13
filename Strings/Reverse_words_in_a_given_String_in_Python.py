a = "Omkar is talented boy"
b = a.split(" ")
print b[::-1]

c = b[::-1]

print " ".join(c)

for i in range(1,len(b)+1):
    print b[-i]