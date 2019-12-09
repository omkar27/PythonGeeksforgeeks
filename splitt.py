from re import split
import re
print(split('\W+', "Word's, words , Words"))

print(split('\W+', 'On 12th Jan 2016, at 11:02 AM'))
print(split('\d+', 'On 12th Jan 2016, at 11:02 AM'))
numstr = "omkar23 hi 54 dslk32 4jvskd sjdflk22 kjkdlf900"
n = re.compile("[0-9]")
print n.findall(numstr)
print set(sorted(n.findall(numstr)))

print split("\d+","On 12th Jan 2016, at 11:02 AM",1)
print split("\w","Aey, Boy oh boy, come here",1,flags=re.IGNORECASE)
print split("\W","Aey, Boy oh boy, come here")