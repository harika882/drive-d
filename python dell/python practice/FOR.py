# Total The Given List Of Values
exp = [2345, 5678, 9867, 4567, 2345, 6546]
mnth = ["jan", "feb", "mar", "april", 'may', 'june']
total = 0
for i in range(len(exp)):
    print("month:", (i + 1), "expence is:", exp[i])
    total = total + exp[i]
print(total)

# Let the check the key is in which place by using for loop
key_match = "bath room"
loc = ["bath room", "dining hall", "kitchen", "chair", "bed room"]
for i in loc:
    if key_match == i:
        print("the key is found at:", i)
        break
    else:
        print("The Key is not found at", i)

# print the numbers between given range
x = (input("enter the starting number"))
y = (input("enter the ending number"))
for i in range(int(x), int(y)):
    if i % 2 == 1:
        continue
    print(i * i)
# print the numbers by using while loop
x = int(input("enter the number"))
i = 0
while i <= x:
    print(i)
    i = i + 1


