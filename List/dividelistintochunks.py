my_list = ['geeks', 'for', 'geeks', 'like',
           'geeky','nerdy', 'geek', 'love',
               'questions','words', 'life']

def divd(l,n):
    print len(l)
    for i in range(0, len(l), n):
        yield l[i:i + n]
n = 5
x = list(divd(my_list,n))
print x
