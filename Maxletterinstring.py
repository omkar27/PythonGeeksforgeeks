st = raw_input("Enter String")
print st.strip()
st = st.replace(" ","")
print list(st)
dc = {}
for i in st:
    print i,st.count(i)
    dc[i] = st.count(i)
print dc
a = list(dc.keys())
b= list(dc.values())
maxval = a[b.index(max(b))]
print maxval