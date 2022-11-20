a = int(input())
b = int(input())
c = int(input())
if a >= b :
    if a >= c :
        print(a)
    else :
        print(c)

elif b >= c :
    if b >= a :
        print(b)
    else :
        print(a)

else :
    if c >= b :
        print(c)
    else :
        print(b)