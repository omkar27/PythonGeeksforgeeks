str ="Omkar"

if 'a' in str and 'e' in str and 'i' in str and 'o' in str and 'u' in str:
    print "Accepted"
else:
    print "Rejected"
count = 0
for i in str:
    if i in 'aeiou':
        count +=1
print count