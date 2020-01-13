a = "OMKAR TERKAR 111"
b = "OMKAR TERKAR 222"
print len(a)
print len(b)
counter  = 0
for i in range(len(a)):
    for j in range(len(a)):
        if(a[i]==b[j]):
            counter +=1
            print a[i]
            break
print counter