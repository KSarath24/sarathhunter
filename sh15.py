s=int(input())
a=input().split()
c=[]
x=0
for i in range(s):
    y=int(a[i])
    c.append(y)
for i in c:
    x=x+i
if(x==0):
    c.sort()
    print(c[s-1])
else:
    print(x)
