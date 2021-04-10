''''
def Zusammen(Liste):
    ListZ = []
    s = input("Gib bitte eine Beziehung mit x = ")
    for i in range(0, len(Liste)):
        l = []
        x = Liste[i]
        y=eval(s)
        print(y)
        if y in Liste:
            l.append(x)
            l.append(y)
            ListZ.append(l)
    print("Elemente mit einem Zusammenhang yreeaaaaah: ", ListZ)
    return

List=[2,4,14,12,3,33,13,44,5,1,26]
Zusammen(List)
def ggt(a,b):
    while b!=0 :
        r=a%b
        a=b
        b=r
    return a

def kgv(a,b):
    return (a*b)/ggt(a,b)

print("der KGV ist",int(kgv(2,4)))

a=int(input("Zahl bitte = "))
b=int(input("Zahl bitte = "))

for i in range (a+1,b+1):
    a = kgv(a,i)
print("der KGV ist = ", int(a))
'''
def BestimmteBeziehung(xy):
    stringg = input("Schreiben Sie die Beziehung zwischen die Zahlen: ")
    return [i for i in xy if eval(stringg.replace("=", "=="), {"x": int(i[0]), "y": int(i[1])})]

List = [20,2,70,33,55,41, 14, 74, 23, 33, 13, 44, 5, 1, 26,66,63]
print(BestimmteBeziehung(xy))