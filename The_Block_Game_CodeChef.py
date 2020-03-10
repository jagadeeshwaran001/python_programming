#link for the problem:-https://www.codechef.com/problems/PALL01
t=int(input())
for _ in range(t):
    a=list(input().strip())
    if(a[0]!=0 and a==a[::-1]):
        print("wins")
    else:
        print("losses")
    
