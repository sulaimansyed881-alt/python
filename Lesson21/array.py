import array as a
a=a.array("i",[9,8,12,68,90])
print(a)
for i in a:
    print(i)
a.append(279)
print(a)
a.remove(68)
print(a)
a.insert(0,101)
print(a)

