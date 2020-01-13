
def even(num):
    ev = 0
    od = 0
    for i in range(num):
        if(i%2==0):
            ev+=1
            print i
        else:
            od +=1
    print "Even Count",ev
    print "Odd count",od

    print "List Comprehension",[no for no in range(num) if no%2==0]

    while (num > 0):
        if (num % 2 == 0):
            print num
        num = num - 1
    a = [1,23,4,5,6,7,8,90,123,345,45,665,7]
    print "Lambda function",list(filter(lambda x:(x%2==0),[2,3,4,5,6,7,8,]))
    print "Lambda Function to count Even Numbers",len(list(filter(lambda x:(x%2==0),[2,3,4,5,6,7,8,])))
    print "Lambda Function to count Odd Numbers", len(list(filter(lambda x: (x % 2 != 0), [2, 3, 4, 5, 6, 7, 8, ])))
    ans = list(filter(lambda x:(x%2==0),[2,3,4,5,6,7,8,]))
    print "ANS",ans
even(27)
