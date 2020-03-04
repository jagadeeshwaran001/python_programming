#link for a problem:-https://www.codechef.com/problems/FLOW004
t=int(input())
for i in range(t):
    a=list(map(int,input().strip()))
    sum=a[0]+a[-1]
    print(sum)