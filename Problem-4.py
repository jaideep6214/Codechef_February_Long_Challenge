t=int(input())
ans=[]
for i in range(t):
    n=int(input())
    w=input()
    w=list(map(int, w.split()))
    l=input()
    l=list(map(int, l.split()))
    if (n==2):
        if (w[0]>w[1]):
            if (l[0]==1):
                ans.append(2)
            else:
                ans.append(1)
        else:
            ans.append(0)
    elif(n==3):
        d={}
        length={}
        jumps=0
        for z in range(3):
            if (w[z]==1):
                d[1]=z
                length[1]=l[z]
            elif(w[z]==2):
                d[2]=z
                length[2]=l[z]
            elif(w[z]==3):
                d[3]=z
                length[3]=l[z]
        while((d[1]>=d[2]) or  (d[2]>=d[3])):
            while (d[1]>=d[2]):
                d[2]+=length[2]
                jumps+=1
            while(d[2]>=d[3]):
                d[3]+=length[3]
                jumps+=1
        ans.append(jumps)
    elif(n==4):
        d={}
        length={}
        jumps=0
        for z in range(4):
            if (w[z]==1):
                d[1]=z
                length[1]=l[z]
            elif(w[z]==2):
                d[2]=z
                length[2]=l[z]
            elif(w[z]==3):
                d[3]=z
                length[3]=l[z]
            elif(w[z]==4):
                d[4]=z
                length[4]=l[z]
        while((d[1]>=d[2]) or  (d[2]>=d[3]) or (d[3]>d[4])):

            while (d[1]>=d[2]):
                d[2]+=length[2]
                jumps+=1
            while(d[2]>=d[3]):
                d[3]+=length[3]
                jumps+=1
            while(d[3]>=d[4]):
                d[4]+=length[4]
                jumps+=1
        ans.append(jumps)
for i in ans:
    print(i)
                    
                
