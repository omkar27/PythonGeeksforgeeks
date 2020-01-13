start = -4
end = 9

for i in range(start,end):
    if(i<0):
        print i

print [i for i in range(start,end+1) if (i<0)]
print list(filter(lambda x: (x<0),range(start,end+1)))