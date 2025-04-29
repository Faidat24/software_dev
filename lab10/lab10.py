"""
Faidat Fahm
April 25, loops
"""
print("\n ------ example 1: for loop as a counter ------")
#print Hello from 0 to 4
for x in range (0,4):
    print(f"Hello = {x}")

print("\n ------ example 2: for loop in a list ------")
fruits = ['apple', 'oranges', 'grapes', 'kiwis', 'pineapple']
for eachfruitindex in range (0,len(fruits)):
        print(f"fruit with index {eachfruitindex} = {fruits[eachfruitindex]}")

# alternative way to loop through a list
print("\n--- Alternative way to loop through a list")
for eachfruit in fruits:
        print(eachfruit)

print("\n ------ example 3: for loop with different increment ------")
# for loop to print from 2 to 30, with an increment of 3    
for num in range (2,30,3):
       print(num)

print("\n ------ example 4: for loop with different decrement ------")
# for loop to print from 10 to 0, with an decrement of 2
for num in range (10,0,-2):
        print(num)

print("\n ------ example 5: for loop through a string------")
username = "yes123"
for eachcharacter in username:
       print(eachcharacter)


print("\n ------ example 6: nested conditional statement------")
#for loop to check how many negative numbers are in the list
numbers = [5, -2, 0, 8, 9, -1]
negativecounter = 0
for eachnumber in numbers:
       if eachnumber <0:
              negativecounter += 1 # the same as negativenumber = negativenumber + 1

# prompt results
print(f"There is/are {negativecounter} negative number/s")

print("\n ------ example 7: nested conditional statement: operation------")
# for loop to add all 'odd' numbers
sumodd = 0
for eachnumber in numbers:
       if eachnumber %2 == 1:
              sumodd += eachnumber

# prompt result
print(f"The sum of all odd numbers is = {sumodd}")

print("\n ------ example 8: break statement in a loop ------")
# for loop to print from 0 to 10(exclusive), and terminate the loop when it reaches to 5
for n in range(0,10):
    if n==5:
       print("counter reaches to 5")
       break
    else:
       print(n)

print("\n ------ example 9: continue statement in a loop ------")
# for loop to add numbers from 0 to 10(exclusive), except number 5
sumall = 0
for n in range(10):
    if n==5:
          print("skipping 5")
          continue
    
    sumall += n
    print(n)
    print(f"\tsum = {sumall}")

print("\n ------ example 10: else statement in a for loop ------")
for n in range(6):
      if (n==3):
            break
      print(n)
else:
      print("Loop completed")

print("\n ------ example 11: while loop as a counter ------")
# while loop to print from 0 to 5(inclusive)--> 0 1 2 3 4 5
n = 0
while n<6:
      print(n)
      n += 1

print("\n ------ example 12: while loop as a checkpoint ------")
# while loop to collect and add numbers between -5 and 5.
# if the user enters a number that is not between -5 and 5, the while will terminate
sumusernumber = 0
while(True):
    number = int(input("Enter a number between -5 and 5: "))
    if number<-5 or number>5: # if not(5>=number>=-5 )
        break
    sumusernumber += number

#prompt result
print(f"The total sum is = {sumusernumber}")

print("\n ------ example 13: while loop as a checkpoint ------")
# while loop to count the even numbers in the list
numbers = [2, 0, -5, 1, 8, -6, 7, -3]
index = 0
len_numbers = len(numbers)
evencount = 0
while index<len_numbers:
      if numbers[index]%2 == 0 and not (numbers[index]==0):
            evencount += 1  
      index += 1
else:
      print(f"There is/are {evencount} even numbers")

            