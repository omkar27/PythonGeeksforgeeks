
def larg(string,k):
    s = string.split(" ")
    news = ""
    ne = []
    for i in s:
        if len(i)>=k:
            news = news +" "+ i
            ne.append(i)
    print news
    print " ".join(ne)

str = "hello geeks for geeks is computer science portal"
k = 4
larg(str,k)