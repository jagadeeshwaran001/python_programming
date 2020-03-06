#linkk for problem:-https://www.codechef.com/problems/TRICOIN
t=int(input())
for _ in range(t):
    n=int(input())
    n=n*2   
    n=-n
    dis = 1-4*n
    root1=(-1 + int(dis**0.5)) / 2
    root2=(-1 - int(dis**0.5))/ 2
    root1=int(root1)
    root2=int(root2)
    if(root1>=0):
        print(root1)
    elif(root2>=0):
        print(root2)
        
