"""for i in range(1,10):
    for n in range(1,i+1):
        print(n,"*",i,"=",i*n,end="  ")
    print()
"""
count = 0
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i == j or j == k or i == k:
                continue
            else:
                print ("{0}{1}{2}".format(i,j,k))
                count += 1
print (count)
