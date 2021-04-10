n=int(input("Zahl="))
ct=0
for i in range(2,n):
    while n%i==0:
        ct+=1
        n=n/i
    if ct>0:
        print("Zahl ")
        print(i)
        print("hoch ")
        print(ct)
    ct=0
#gata