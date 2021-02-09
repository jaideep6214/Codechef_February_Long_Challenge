def different(l1,l2):
    s=len(set(l1+l2))
    return s
t=int(input())
ans=[]
for i in range(t):
    n=int(input())
    words=input()
    words=words.split()
    d={}
    for w in words:
        if (w[1:] in d):
            d[w[1:]].append(w[0])
        else:
            d[w[1:]]=[w[0]]
    
    keys=list(d.keys())
    print(d,keys)
    
    temp=0
    for x in range(len(d)):
        for y in range(x+1,len(d)):
            j=different(d[keys[x]],d[keys[y]])
            print(j)
            temp+=(j-len(d[keys[x]]))*(j-len(d[keys[y]]))
            print((j-len(d[keys[x]]))*(j-len(d[keys[y]])))
    ans.append(temp*2)
for i in ans:
    print(i)
