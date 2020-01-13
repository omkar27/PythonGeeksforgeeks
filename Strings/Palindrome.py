a= "Omkar"
b = a[::-1]
if a==b:
    print "true"
else:
    "false"
c = ""
le = len(a)
for i in range(1,le):
    print a[i]
    c = c + a[-i]
    if c == a:
        print "True"
    else:
        print "False"
print c

print list(reversed(a))