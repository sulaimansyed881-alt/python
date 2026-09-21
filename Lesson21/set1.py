m={4,"Enter",9.78,False}
n={9,8,7,0}
print(m)
print(n)
for i in m:
    print(i)
print("The length is",len(n))
m.add(89)
n.add(6)
print(n)
print(m)
m.clear()
print("The length of m is",len(m))
n.remove(7)
n.remove(0)
print(n)