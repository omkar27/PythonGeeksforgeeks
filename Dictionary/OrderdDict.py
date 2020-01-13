from collections import OrderedDict
input = 'engineers rock'
pattern = 'egr'

dict = OrderedDict.fromkeys(input)
print dict

ptrlen = 0
print pattern[ptrlen]
for key,val in dict.items():
    if(key == pattern[ptrlen]):
        ptrlen = ptrlen+1

        if(ptrlen == len(pattern)):
            print 'True'
    else:
        print 'False'