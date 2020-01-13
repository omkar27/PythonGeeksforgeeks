import re
def pata(text):
    pattern = "ab"
    if re.search(pattern,text):
        print "Matched"
    else:
        print "Not Matched"
if __name__ == '__main__':
    pata("OMkar")
