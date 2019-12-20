# # finding even, odd and prime numbers
# lower=int(input("Enter the lower limit"))
upper=int(input("enter the upper limit"))
# print("the even numbers are:")
# for num in range(lower,upper+1):
#         if num%2==0:
#             print(num)
# print("the odd numbers are:")
# for num in range(lower, upper + 1):
#         if num%2==1:
#             print(num)
count=0
for num in range(upper):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break

        else:
            count = count + 1
            print("the",count,"prime number is:",num)

# # finding given number is armstrong number or not
# # ARMSTRONG NUMBER:ACTUAL NUMBER IS EQUALS TO SUM OF NTH POWER OF ITS DIGITS.
# for i in range(200):
#     num=i
#     result=0
#     n = len(str(i))
#     while(i!=0):
#         k=i%10
#         result=result+k**n
#         i=i//10
#     if num==result:
#         print(num)
#
# # fibonacci series
# # 0,1,1,2,3,5,8,13,21,33. . . .
# first=0
# second=1
# for i in range(10):
#     print(first)
#     temp=first
#     first=second
#     second=temp+second
# # factoraial of a number
# a=int(input("enter the number"))
product=1
a=int(input("enter the factorial number:"))
for i in range(a):
    product=product*(i+1)

print(a,"factorial is:",product)
