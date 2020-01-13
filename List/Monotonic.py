#Monotonic array is array which constant increament or decrement
a = [3,4,5,6,7,8,9]
#all return boolean val if given condition will true for loop else will return false
print all(a[i]<=a[i+1] for i in range(len(a)-1) or a[i]>=a[i+1] for i in range(len(a)-1))