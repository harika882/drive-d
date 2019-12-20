'''to take the values in a maatrix in list'''
r=int(input("enter the no.of rows"))
c=int(input("enter thee no.of coloumns"))
for i in range(r):
    m.append([])
    for j in range(c):
        m[i].append(j)
        print("enter the row",i+1,"coloumn",j+1)
        m[i][j]=int(input())
print(m)
# sum of two matrices

# a=int(input("enter the no.of rows"))
# b=int(input("enter the no.of coloumns"))
# c=[[int(input("enter the matrix1:"))for j in range(b)]for i in range(a)]
# d=[[int(input("enter the matrix2:"))for j in range(b)]for i in range(a)]
# e=[[0for j in range(b)]for i in range(a)]
# print("matrix1")
# for i in range(a):
#     for j in range(b):
#         print(c[i][j])
# print
# print("matrix2")
# for i in range(a):
#     for j in range(b):
#         print(c[i][j])
#     print
# print("sum of two matrices is")
# e[i][j]=0
# for i in range(a):
#     for j in range(b):
#         e[i][j]=c[i][j]+d[i][j]+e[i][j]
# print(e[i][j])

# r=int(input("enter the rows"))
# c=int(input("enter the coloumns"))
# a=[[1,2],[3,4],[4,5]]
# for i in range(0,r):
#     for j in range(0,c):
#         a[i]+a[j]
#         print(a)
# interchanging the elements in the lists
l1=[2,4,6,8]
l2=[3,5,7,9]
print("before interchanging:")
print(l1)
print(l2)
# using third variable
# temp1=l1[3]
# temp2=l1[0]
# l1[0]=l2[3]
# l2[3]=temp2
# l1[3]=l2[0]
# l2[0]=temp1
# without using third variable
l1[0],l2[3]=l2[3],l1[0]
l2[0],l1[3]=l1[3],l2[0]
print("after interchanging:")
print(l1)
print(l2)