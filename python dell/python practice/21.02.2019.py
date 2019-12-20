#multiples of 3 except multiples of 5
i=1
a=int(input("enter the limit"))
while i<=a:
    if i%3==0:
        if i%5!=0:
            print(i)

    i=i+1

# multiples of 7
a=7
b=0
i=1
j=int(input("enter the limit"))
while i<=j:
    if i%7==0:
        b=b+1
        print(a,"*",b,"=",i)
    i=i+1