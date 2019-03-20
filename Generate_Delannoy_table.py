import numpy as np

#m=np.array((5,5))
#print("Original array:")
#print(m)

# m is collumn and n is number of rows

n=7
m=6
a=[]
z=1


for k in range(n):
    a.append([z]*m)

print(a)
print('')

for i in range(1,n):
    for j in range(1,m):
        a[i][j] = a[i-1][j] + a[i-1][j-1] + a[i][j-1]

    print(a[i-1])
    print('')





