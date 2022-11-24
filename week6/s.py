def s(a,n):
    d={}
    for i in a:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    power=0
    length=[]
    for i in d:
        if d[i]>power:
            power=i
    for j in range(0,len(a)):
        x=a[0:j]
        m={}
        s=0
        for i in x:
            if i not in m:
                m[i]=1
            else:
                m[i]+=1
        for i in m:
            if m[i]>s:
                s=i        
        if power==s:
           length.append(len(x))
    return min(length)     

