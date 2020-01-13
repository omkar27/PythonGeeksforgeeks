ones = ["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen","fourteen",
        "fifteen","sixteen","seventeen","eighteen","nineteen","twenty"]
tens = ["thirty","fourty","fifty"]

num =20
ans = None
c = " "
while(num>0):
    ans = num%10
    if(num>10 and num<21):
        print ones[(ans+10)-1]
        break
    else:
        c = str(ans) + c
        print ans
       # print ones[ans-1]

    num = num/10
print c
