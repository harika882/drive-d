for r in range(8):
    for c in range(8):
        if (c==0 or c==7)or ((r==0 or r==4) and (c>0 and c<7)):
            print("*",end="")
        else:
            print(end=" ")

    print()

for r in range(6):
    for c in range(6):
        if (c==0 or c==5)or r==c:
            print("*",end="")
        else:
            print(end=" ")
    print()
for r in range(6):
    for c in range(6):
        if r==0 or r==5 or c==3:
            print("*",end="")
        else:
            print(end=" ")
    print()
print("\n")
for r in range(6):
    for c in range(6):
        if c==0 or r==5:
            print("*",end="")
        else:
            print(end=" ")
    print()
print("\n")
i=0
j=4
for r in range(7):
    for c in range(5):
        if c==0 or (r==c+2 and c>1):
            print("*",end="")
        elif((r==i and c==j) and c>0):
            print("*",end="")
            i=i+1
            j=j-1
        else:
            print(end=" ")
    print()
print(f"\n")
for r in range(6):
    for c in range(6):
        if c==0 or c==5 or r==5:
            print("*",end="")
        else:
            print(end=" ")
    print()
for r in range(6):
    for c in range(6):
        if c==0 or c==4:
            print("*",end="")
        elif (r==c and c<3) or (r==1 and c==3):
            print("*",end="")
        else:
            print(end=" ")
    print()
for r in range(8):
    for c in range(8):
        if (c==0 or c==7)or ((r==0 or r==4) and (c>0 and c<7)):
            print("*",end="")
        else:
            print(end=" ")

    print()
i=0
j=6
for r in range(7):
    for c in range(7):
        if (c==0) or (r==c+2 and c>1):
            print("*",end="")
        elif((r==i and c==j) and c>0):
            print("*",end="")
            i=i+1
            j=j-1
        elif r==0:
            print("*",end="")
        else:
            print(end=" ")
    print()
