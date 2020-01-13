name = "Omkar"

print type(reversed(name))
print list(reversed(name))
n = "".join(list(reversed(name)))
print n
if n.lower() == name.lower():
    print True
else:
    print False
