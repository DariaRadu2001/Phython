v=[8,5,7,8,2,1,6,2]
prim = 1
lung=1
max=1
a=v[0]
for i in v:
    if i>a:
        diff = i - a
        for j in range(2, diff):
            if diff % j == 0:
                prim = 0

        if prim == 1:
            lung += 1

        if prim == 0:
            if lung > max:
                 max = lung
            lung = 0
        prim = 1


    if i<a:
        diff = a - i
        for j in range(2, diff):
            if diff % j == 0:
                prim = 0

        if prim == 1:
            lung += 1

        if prim == 0:
            if lung > max:
                max = lung
            lung = 0
        prim = 1
    a=i


if lung>max:
    max=lung
print(max)
#gata