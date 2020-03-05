#link for the problem:-https://www.codechef.com/submit/FLOW007
t=int(input())
for _ in range(t):
    n=int(input())
    rev = 0
  
    while(n > 0): 
        a = n % 10
        rev = rev * 10 + a 
        n = n // 10
      
    print(rev)
   
