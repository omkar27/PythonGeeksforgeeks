a = "OMakrsfjsdfnsjfkjnadkjnakldnkhdaihakahdadaeiuo"

b = set(a)
counter = 0
for i in b:
    if i in "aeiou":
        counter +=1
print counter

