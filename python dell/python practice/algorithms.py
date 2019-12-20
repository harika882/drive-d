# # sorting by section sort algorithm
l1=[]
for i in range(int(input("enter the range"))):
    l1.append(int(input()))
print("before sorting:",l1)
for i in range(len(l1)):
    min_val=min(l1[i:])
    min_ind=l1.index(min_val)
    l1[i],l1[min_ind]=l1[min_ind],l1[i]
print("after sorting:",l1)
# sorting by bubble sort algorithm
# l1=[]
# num=int(input("how many values u want to enter the list:"))
# print("enter the values:")
# for i in range(num):
#     l1.append(int(input()))
# for j in range(len(l1)):
#     for i in range(len(l1)-1):
#         if l1[i]>l1[i+1]:
#             l1[i],l1[i+1]=l1[i+1],l1[i]
#
# print(l1)
#
