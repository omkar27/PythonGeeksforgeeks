# initializing lists
test_list1 = [1, 3, 4, 6, 8]
test_list2 = [4, 5, 6, 2, 10]
res = []
for i in range(len(test_list1)):
    print test_list1[i]*test_list2[i]
    res.append(test_list1[i]*test_list2[i])
print res

print [test_list2[i]*test_list1[i] for i in range(len(test_list1))]