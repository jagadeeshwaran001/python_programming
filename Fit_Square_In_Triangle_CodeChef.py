#link for the problem:-https://www.codechef.com/problems/TRISQ
t=int(input())
for _ in range(t):
    b=int(input())
    b=(b//2)-1
    b=(b*(b+1))/2
    print(int(b))
