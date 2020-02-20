def fo(start,end):
    count=0
    for i in range(start,end,2):
        count=count+1
    print(count)

t = int(input())
for i in range(t):
    a=list(map(int, input().split(":")))
    if(a[1]==2):
        if(a[0]%100==0):
            if(a[0]%400==0):
                fo(a[2],30)
            else:
                fo(a[2],60)
        elif(a[0]%4==0):
            fo(a[2],30)
        elif(a[0]%4!=0):
            fo(a[2],60)
    if(a[1]<=7 and a[1]%2==0 and a[1]!=2):
        fo(a[2],62)
    elif(a[1]<=7 and a[1]%2!=0 and a[1]!=2):
        fo(a[2],32)
    if(a[1]>7 and a[1]%2==0):
        fo(a[2],32)
    elif(a[1]>7 and a[1]%2!=0):
        fo(a[2],62)