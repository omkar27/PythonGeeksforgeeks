import re
#Regular Expression pattern 'ub' matches the string at "Subject" and "Uber".
print re.sub("ub","*~","Subject has Uber booked already",flags=re.IGNORECASE)
# Consider the Case Senstivity, 'Ub' in "Uber", will not be reaplced.
print re.sub("ub","*~","Subject has Uber booked already")
# As count has been given value 1, the maximum times replacement occurs is 1
print re.sub("ub","*~","Subject has Uber booked already",count=2,flags=re.IGNORECASE)
# 'r' before the patter denotes RE, \s is for start and end of a String.
print re.sub(r"\sAnd\s"," & ","Baked Beans And Spam")
print re.sub("And","&","Baked Beans And Spam")
