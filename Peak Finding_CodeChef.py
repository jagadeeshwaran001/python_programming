try:
    t=int(input())
    for i in range(t):
        n=int(input())
        l=[]
        for j in range(n):
            l.append(int(input()))
        print(max(l))
except:
    pass