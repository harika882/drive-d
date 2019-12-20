import datetime
x=datetime.datetime.now()
print(datetime.datetime.now())
t1=datetime.time()
print(t1)
print(x.year,x.time(),x.date(),x.day,x.hour)
i=1
a=int(input("enter the limit"))
while i<=a:
    if i%3==0:
        if i%5!=0:
            print(i)

    i=i+1

t2=datetime.time()
print(t2)
print(t2-t1)
