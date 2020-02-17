def fun(k,fla,c):
    if(len(c)==1):
        return(c)
    elif(fla<=k):
        del(c[fla-1])
        c=c[fla:]+c[:fla]
        return(c)
    elif(fla>k):
        while(fla>k):
            fla=fla-k
        del(c[fla-1])
        c=c[fla:]+c[:fla]
        print("c",c)
        return(c)
a=list(input('first name :').strip())
b=list(input('second name :').strip())
c=['f','l','a','m','e','s']
le=len(a)
el=len(b)
for i in a:
        if(i in b):
            le=le-1
            el=el-1
fla=le+el
print('fla:',fla)
for k in range(6,0,-1):
    app=fun(k,fla,c)
if(app[-1]=='f'):
    print('friends :) :)')
elif(app[-1]=='l'):
    print('love :) :) :)')
elif(app[-1]=='a :)'):
    print('affection')
elif(app[-1]=='m'):
    print('**Marrige** ()')
elif(app[-1]=='e'):
    print('enemies :( :(')
elif(app[-1]=='s'):
    print('sister :(')
else:
    print("error occored")