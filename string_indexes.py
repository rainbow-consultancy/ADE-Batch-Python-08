# indexing 

name = "Python" 

# Positiv Indexing -> [P=0, y=1, t=2, h=3, o=4, n=5]
# Negative Indexing -> [-1=n, -2=o, -3=h, -4=t, -5=y, -6=P]

print(name[0])

# syntax 
# var[start: stop: step=1]

print(name[3])
print(name[5])

print(name[0:3])
# print(name[8]) # fails

print(name[0:3:2])
print(name[0:6:3])
print(name[:])
print(name[::1])
print(name[::])
print(name[::2]) # Pto

print(name[-1])
print(name[-1:-4:-1])
print(name[::-1])







