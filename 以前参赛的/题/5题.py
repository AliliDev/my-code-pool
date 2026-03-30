a=[3, 7, 5, 8, 2]
b=[5,7,9]
for i in a:
    if i in b:     #不是not in
        b.append(i)
print(b)
