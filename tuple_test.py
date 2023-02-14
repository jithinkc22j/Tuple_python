# creating an empty tuple
t=tuple()
#Tuple Functions
t = (1, 2, 3, 4, 5, 6, 7, 8, 9, 5)
print(len(t))
print(t.count(5))
print(any(t))
print(min(t))
print(max(t))
print(sum(t))
print(sorted(t))
print(t[5])
del t

#Common tuple operations
T = (1, 2, 3, 4, 5, 6)
L = (7, 8, 9, 10)
print(T + L)
print(T[0:3])
print(2 * T)
print(3 in T)
print(30 not in T)

# Traversing a tuple
T = (1, 7, 2, 3)
for i in T:
    print(i)
