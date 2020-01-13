lst = [True,False,False,True,True,False]

print "False index for list {}".format(lst)
for k,i in enumerate(lst):
    if not i:
        print k,
print [k for k,i in enumerate(lst) if not i]

print list(filter(lambda x:not in lst[x],len(lst)))
