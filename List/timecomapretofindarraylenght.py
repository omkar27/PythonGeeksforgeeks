import time
a = [2,3,4,5,6,7,8,2,3]


counter = 0

start_naive = time.time()
for i in a:
    counter = counter + 1
print counter
end_naive = start_naive - time.time()

start_len = time.time()
le = len(a)
print le
end_len = start_len - time.time()

start_hint = time.time()
# l = length_hint(a)
# print l
end_hint = start_hint - time.time()

print "Naive",end_naive
print "Len",end_len
print "Hint",end_hint
