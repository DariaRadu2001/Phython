import random
def dict():
    d={}
    return d

def Wiederholung(Liste):
    d=dict()
    for i in Liste:
        if i in d:
            Liste.remove(i)
        else:
            d[i]=1
    return Liste

def creatRandomList():
    randomlist = []
    for i in range(0,11):
        n = random.randint(10,99)
        randomlist.append(n)
    return(randomlist)

def Symmetrie(Liste):
    ct=0
    ListeS=[]
    for i in Liste:
        listS=[]
        listS.append(i)
        ct+=1
        x=i%10*10+i//10
        for j in range(ct, len(Liste)):
            if Liste[j]==x:
                listS.append(x)
                ListeS.append(listS)
    print("Symmetrieliste ist :",ListeS,"hat ", len(ListeS)," Elementen")
    return

def Konk(Liste):
    l=[]
    for i in range(0,len(Liste)):
        l.append(Liste[i])
    l.sort(reverse=True)
    x=0
    for i in range(len(l)):
        x= x*100+l[i]
    return x

def Krypto(Liste):
    key=Liste[0]
    l=[]
    for i in range(1,len(Liste)):
        l.append(Liste[i]+key)
    return l

'''
def Zusammenhang(Liste):
    ListZ=[]
    for i in range(0, len(Liste)):
        l = []
        y=Liste[i]
        x=y+10
        if x in Liste:
            l.append(y)
            l.append(x)
            ListZ.append(l)
    print("Elemente mit einem Zusammenhang: ", ListZ)
    return
'''

def Zusammenhang(Liste, Beziehung):
    ListZ = []
    for i in range(0, len(Liste)):
        l = []
        x = Liste[i]
        y=eval(Beziehung)
        if y in Liste:
            l.append(x)
            l.append(y)
            ListZ.append(l)
    return ListZ


def Domino(Liste):
    lung = 1
    max = 1
    a = Liste[0] #nr precedent
    l=[]
    lmax=[]
    l.append(a)
    for i in range(1, len(Liste)):
        x=Liste[i] #nr actual
        if x//10 == a%10:
            lung += 1
            l.append(x)
        else:
            if lung > max:
                lmax=[]
                for j in range(0, len(l)):
                    lmax.append(l[j])
                max = lung
            lung = 1
            l.clear()
            a = Liste[i]
            l.append(a)
        a = Liste[i]
    if lung > max:
        max = lung
        lmax=[]
        for i in range(0, len(l)):
            lmax.append(l[i])
    if max==1:
        print("Es gibt kein Domino")
    else:
        print("Die größte Länge ist: ",max," die Liste ist:" ,lmax)
    return max

def ggt(a,b):
    while b!=0 :
        r=a%b
        a=b
        b=r
    return a

def kgv(a,b):
    return (a*b)/ggt(a,b)

def KGV():
    a = int(input("Zahl bitte = "))
    b = int(input("Zahl bitte = "))

    for i in range(a + 1, b + 1):
        a = kgv(a, i)
    return a

def main():
    Liste=creatRandomList()
    print("Die vollstandige Liste ist:       ",Liste)
    print("Die Liste ohne Wiederholungen ist:",Wiederholung(Liste))
    Symmetrie(Liste)
    print("Die Konk. der Zahlen ist: ",Konk(Liste))
    print("Krypto Liste : ",Krypto(Liste))
    List=[2,4,14,12,3,33,13,44,5,1,26]
    s = input("Gib bitte eine Beziehung mit x = ")
    print("Elemente mit einem Zusammenhang : ", Zusammenhang(List,s))
    print("Elemente mit einem Zusammenhang : ", Zusammenhang(Liste,s))
    List = [20,2,70,33,55,41, 14, 74, 23, 33, 13, 44, 5, 1, 26,66,63]
    Domino(Liste)
    Domino(List)
    print("der KGV ist = ", int(KGV()))
main()

