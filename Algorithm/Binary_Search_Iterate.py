import pdb


def bin(lis,x):
    print "OMKAR"
    start_point = 0
    end_point = len(lis)-1
    print "EEEENNNNDDDDDD",end_point
    while start_point <= end_point:
         #print "EP",end_point
         #print "SP",start_point
         mid = start_point +  (end_point - start_point) // 2
         print "MIDDLE",mid
         print "LIST MIDDLE",lis[mid]
         val = lis[mid]
         if val == x:
             print "Number {} Found at index {}".format(x,mid)
             break
         elif val > x:
            print "Val greter"
            end_point = mid - 1
            print end_point
         elif val < x:
             print "Val less"

             start_point = mid + 1
             print start_point

lis = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
x = 14
bin(lis,x)