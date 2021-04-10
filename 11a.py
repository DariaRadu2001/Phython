def prim(a):
    pr=1
    for b in range(2, a//2):
        if a % b == 0:
            pr = 0
            break
    if pr == 1:
         return True
    else:
         return False

n=int(input("Zahl="))
ct=0
i=3
while ct != n:
    if prim(i)==True:
            j=i+2
            if prim(j)==True:
                print("( %d , %d )"%(i,j))
                ct+=1
                i=j
            else:
                i+=1
    else:
        i+=1
#gata