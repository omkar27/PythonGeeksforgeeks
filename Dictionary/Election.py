from collections import Counter
votes= {"john", "johnny", "jackie",
           "johnny", "john", "jackie",
           "jamie", "jamie", "john",
           "johnny", "jamie", "johnny",
           "john"}
print dict(Counter(votes))
