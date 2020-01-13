import re

string = "Omkar"
def check(string):
    regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if regex.search(string):
        print "Rejected"
    else:
        print "Accepted"

string=raw_input()
check(string)