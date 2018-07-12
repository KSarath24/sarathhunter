s=[str(i) for i in input().split()]
x=len(s)
for i in range(0,x):
    print(s[i][::-1],end=' ')
