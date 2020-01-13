class spltnjoin:

    def __init__(self,st):
        self.st = st

    def splitstr(self):
        self.st = self.st.split(" ")
    def joinstr(self):
        self.st = "-".join(self.st)
        print self.st
if __name__ == '__main__':
    st = "Omkar is good boy."
    sp = spltnjoin(st)
    sp.splitstr()
    sp.joinstr()
    st = ['Geeks', 'for', 'Geeks']
    sp = spltnjoin(st)
   # sp.splitstr()
    sp.joinstr()