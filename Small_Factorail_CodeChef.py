#link for the problem:-https://www.codechef.com/problems/FCTRL2
t=int(input())
for _ in range(t):
    n=int(input())
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(fact)
        