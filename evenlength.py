str = "This is a python language"
f= open("guru99.txt","w+")
for i in range(10):
     f.write("This is line %d\r\n" % (i+1))
f.close()

f=open("guru99.txt", "r")
if f.mode == 'r':
    contents = f.read()
print contents
print list(str)
arr = " ".join(list(str))
print arr