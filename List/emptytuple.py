a = [(23,43),(),(43,54),(9,43),()]
for i in a:
    if i:
        print i

print filter(None,a)

print [i for i in a if i]

print [filter((lambda x:x),a)]