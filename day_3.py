# Exercises Day #3

# Control Flow with if/else and Conditional Operators

# Create a program for height requirement to ride a rollercoaster

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster.")
else:
  print("Sorry, you will need to meet the requirement.")

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

# Write a program that works out whether if a given number is an odd or even number.
number = int(input("Which number do you want to check? "))

if number % 2 == 0:
    print("This is an Even number.")
else:
    print("This is an Odd number.")

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

# Nested if statements and elif statements

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 115:
    print("You can ride the rollercoaster.")
    age = int(input("What is your age? "))
    if age <= 17:
        print('Your payment is $15')
    elif age <= 13:
        print('Your payment is $3')
    else:
        print("Your payment is $25")
else:
  print("Sorry, you will need to meet the requirement.")

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February.

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
  if year % 100 ==0:
    if year % 400 == 0:
      print("Leap Year")
    else:
      print("Not Leap year")
  else:
    print("Leap Year")
else:
  print("Not Leap Year.")

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

# From the previous Nested if statements and elif statements, going to add if they want to purchase pictures.

bill = 0
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 115:
  print("You can ride the rollercoaster.")
  age = int(input("What is your age? "))
  if age <= 17:
    bill = 15
    print('Your payment is $15')
  elif age <= 13:
    bill = 3
    print('Your payment is $3')
  else:
    bill = 25
    print("Your payment is $25")
  purchase_photo = input("Do want you want to purchase your photos? Y  or N: ")
  if purchase_photo == "Y":
    bill += 1
  print(f"Your final bill is: ${bill}")    
else:
  print("Sorry, you will need to meet the requirement.")

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
# Create a program where you are completing a pizza order.

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if size == "S":
    bill += 15
    if add_pepperoni == 'Y':
        bill += 2
    if extra_cheese == 'Y':
        bill += 1
elif size == 'M':
    bill += 20
    if add_pepperoni == 'Y':
        bill += 3
    if extra_cheese == 'Y':
        bill += 1
else:
    bill += 25
    if add_pepperoni == 'Y':
        bill += 3
    if extra_cheese == 'Y':
        bill += 1
print(f'Your final bill is: ${bill}.')

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
 
# Logical Operators

bill = 0
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
if height >= 115:
  print("You can ride the rollercoaster.")
  age = int(input("What is your age? "))
  if age <= 17:
    bill = 15
    print('Your payment is $15')
  elif age <= 13:
    bill = 3
    print('Your payment is $3')
  elif age >= 45 and age <= 55:
    print('Enjoy your free ride')
  else:
    bill = 25
    print("Your payment is $25")
  purchase_photo = input("Do want you want to purchase your photos? Y  or N: ")
  if purchase_photo == "Y":
    bill += 1
  print(f"Your final bill is: ${bill}")    
else:
  print("Sorry, you will need to meet the requirement.")

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combine_name = name1 + name2
lower_case_letter = combine_name.lower()

t = lower_case_letter.count('t')
r = lower_case_letter.count('r')
u = lower_case_letter.count('u')
e = lower_case_letter.count('e')

true = t + r + u + e

l = lower_case_letter.count('l')
o = lower_case_letter.count('o')
v = lower_case_letter.count('v')
e = lower_case_letter.count('e')

love = l + o + v + e

love_score = int(str(true) + str(love))

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(love_score)

print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")

# Creating a Treasure Island Program

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice1 = input('Which direction? "left" or "right" ').lower()

if choice1 == "left":
    choice2 = input('At the Lake, "boat" or "swim" ').lower()
    if choice2 == "boat":
        choice3 = input('which color door? "blue", "red" and "yellow" ').lower()
        if choice3 == "blue":
            print("Alert, Alert, Grab your Treasure")
        elif choice3 == "red":
            print("Room full of fire, Game Over")
        elif choice3 == "yellow":
            print("Opps, not quite, Game Over")
    else:
            print("Fell Through, Game Over")
else:
    print("Wrong choice, Game Over")

