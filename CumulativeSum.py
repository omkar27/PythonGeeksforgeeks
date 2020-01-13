import re
arr = [10, 20, 30, 40, 50]
newarr = []
sum = 0
for i in range(len(arr)):
    sum = sum + arr[i]
    newarr.append(sum)
print newarr

name = "Omkar"
print name.find('r')

para = "My Email is omkarterkar27@gmail.com"
lst = re.findall("\S+@+\S+.+\S",para)
print lst

