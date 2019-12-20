# finding the given number is even or odd
num=int(input("enter a number"))
if num%2==0:
    print("the given number is even")
else:
    print("the given number is odd")
# finding the given value in the following lists
indian=["aloo","chapathi","dosa"]
chineese=["parota","gobi manchooriya","noodles"]
italian=["pizza","bugger","spring roll"]
food=input("enter the food name")
if food in indian:
    print("The Food Is Indian Food")
elif food in chineese:
    print("The Food Is Chineese")
elif food in italian:
    print("The Food Is Italian")
else:
    print("I dont recognize the given food is which type of food")

USA=["atlanta","new york","chicago","baltimore"]
UK=["london","BRISTAL","CAMBRIDGE"]
INDIA=["Mumbai","delhi","bangalore"]
name=input("Enter The City Name")
# finding the given value in the lists
if name in USA:
    print("The City in USA")
elif name in UK:
    print("The City in UK")
elif name in INDIA:
    print("The City in India")
else:
    print("Sorry, I Don't recognize the city in which country")

name1=input("enter the first city")
name2=input("enter the second city")
if name1 and name2 in USA:
    print("they both are in USA")
elif name1 and name2 in UK:
    print("They both are in UK")
elif name1 and name2 in INDIA:
    print("They both are in india")
else:
    print("The given two CITIEs are not in same country")