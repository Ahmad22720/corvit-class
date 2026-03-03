t=(1,2,3,4,5,6,1,1,2,4)
print(type(t))
#count function counts the value available in the tuple
x=t.count(1)
# index function show the nost first index available in the tuple
y=t.index(6)
print(x)
print(y)
z=list(t)
t=(1,2,3,4,5,6,6,99,'apple')
z=tuple(t)
print(type (t))
print(t)