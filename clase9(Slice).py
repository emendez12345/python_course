a=[250,12,4,78,89]
b=a
print(a)
print(b)
del a[0]
print(id(a))
print(id(b))
c=a[:]
print(id(a))
print(id(b))
print(id(c))
a.append(6)
print(id(a))
print(id(b))
print(id(c))



