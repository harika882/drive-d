def age_dictionary():
    '''this function asks the person to enter
     name and age later this program will say
      the age of the given person'''
d={}
while True:
    person=input("enter the person name,to stop dont enter anything and hit enter key.")
    if person=='':
        break
    age=input("enter age")
    d[person]=age
while True:
    person=input("now enter the person name i will say his/her age")
   if name=='':
    break
if person in d:
    print("age of",person,"is",d[person])
else:
    print("i don't know age of",person)
    print("age dictionary program is finished")
    age_dictionary()