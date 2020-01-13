str1 = 'Omkar27dada'
str2 = 'Omkardada'
newstr = ''
for i in range(len(str1)):
    for j in range(len(str2)):
        if str1[i] == str2[j]:
            newstr = newstr + str1[i]
            print str1[i],
print set(newstr)