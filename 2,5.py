def ggt(a,b):
    while b!=0:
        r=a%b
        a=b
        b=r
    return a

v=[4,2,14,7,3,5,21,7,8]
c=v[0]
lange=1
max=1
for i in range(1,len(v)):
    if ggt(c,v[i])==1:
        lange+=1
    elif max<lange:
        max=lange
        lange=1
    else:
        lange=1
    c=v[i]
print(max)
#gata
