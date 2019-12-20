#fibonacci series by python program
# 0 1 1 2 3 5 8 13 21 34 . . . .
n=int(input("enter the series limit:"))
a=0
b=1

if n==0:
    print("it is not possible")
elif n<2:
    print(a)
elif n>=2:
    print(a)
    print(b)
for i in range(n-2):
    c=a+b
    print(c)
    a=b
    b=c

