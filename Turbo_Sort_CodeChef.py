#link for a problem:-https://www.codechef.com/problems/TSORT
n=int(input())
a=[]
for i in range(n):
    a.append(int(input()))
a=sorted(a)
for i in range(n):
    print(a[i])