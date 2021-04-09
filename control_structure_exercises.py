#Do your work for this exercise in a file named control_structures_exercises.py.

#Conditional Basics

    #1a.) prompt the user for a day of the week, print out whether the day is Monday or not
day_of_the_week = input('What day is it today?')
day_of_the_week = day_of_the_week.lower()
if day_of_the_week == ('monday'):
  print('Today is Monday')
else:
  print('Today is not Monday');

    #1b. )prompt the user for a day of the week, print out whether the day is a weekday or a weekend
day_of_the_week = input('What day is it today?')
day_of_the_week = day_of_the_week.lower()
if day_of_the_week in ['saturday', 'sunday']:
  print('It is a weekend today')
else:
  print('It is a weekday today');

    #1c.)create variables and make up values for:
#the number of hours worked in one week
#the hourly rate
#how much the week's paycheck will be
#write the python code that calculates the weekly paycheck. 
# You get paid time and a half if you work more than 40 hours

hours_worked = 41
hourly_pay = 14
overtime_hours = hours_worked - 40
if hours_worked <= 40:
    paycheck = hours_worked * hourly_pay
else:
    paycheck = (((hourly_pay // 2) + hourly_pay) * overtime_hours) + (hours_worked * hourly_pay)
               
print(paycheck)

#Loop Basics
#a.)While
#Create an integer variable i with a value of 5.
#Create a while loop that runs so long as i is less than or equal to 15
#Each loop iteration, output the current value of i, then increment i by one.
i = 5
while i <= 15:
    print(i)
    i +=1

#Create a while loop that will count by 2's
# starting with 0 and ending at 100. Follow each number with a new line.
i = 0
while i <=100:
    print(i)
    i+=2

#Alter your loop to count backwards by 5's from 100 to -10.   
i = 100
while i>=-10:
    print(i)
    i-=5           

#Create a while loop that starts at 2, 
# and displays the number squared on each line while the number is less than 1,000,000. Output should equal:
i = 2
while i < 1000000:
    print(i)
    i*=i

#Write a loop that uses print to create the output shown below. Counts down by 5 from 100, stops at 5. 
i = 100
while i >= 5:
    print(i)
    i-=5

#For Loops
#B1.) Write some code that prompts the user for a number,
# then shows a multiplication table up through 10 for that number.
select_number = int(input("Type a number: "))
for i in range(1,11):
    print(select_number, 'x', i, '=', select_number*i)

#B2.)Create a for loop that uses print to create the output shown below.
for n in range(1,10):
    print(f'{n}' * n)

#C1.)Prompt the user for an odd number between 1 and 50. 
# Use a loop and a break statement to continue prompting the user if they enter invalid input.
#  (Hint: use the isdigit method on strings to determine this). Use a loop 
# and the continue statement to output all the odd numbers between 1 and 50, except for the number the user entered.
userInput = int(input('Number to skip is: '))
while userInput % 2 == 0:
    userInput = int(input('Number to skip is: '))
for num in range(1, 50, 2):
    if(num != userInput):
        print('Here is an odd number: {}'.format(num))
    else:
        print('Yikes! skipping number: {}'.format(userInput))

#C2.)The input function can be used to prompt for input and use that input in your python code. 
# Prompt the user to enter a positive number and write a loop that counts from 0 to that number. 
prompt = int(input('Enter a positive number:'))
start = 0
while start < (prompt + 1):
    print(start)
    start += 1
#C3.) Write a program that prompts the user for a positive integer. 
# Next write a loop that prints out the numbers from the number the user entered down to 1.
prompt = int(input('Enter a positive number'))
while prompt >= 1:
    print(prompt)
    prompt -= 1

#3.)Write a program that prints the numbers from 1 to 100.
    #For multiples of three print "Fizz" instead of the number
    #For the multiples of five print "Buzz".
    #For numbers which are multiples of both three and five print "FizzBuzz".
for n in range(1,101):
    
    if n % 15 == 0:
        print('FizzBuzz')
        continue
    elif n % 3 == 0:
        print('Fizz')
        continue
    elif n % 5 == 0:
        print('Buzz')
        continue
    else:
        print(n)


#4.) Display a table of powers.
# Display a table of powers.
#Prompt the user to enter an integer.
#Display a table of squares and cubes from 1 to the value entered.
#Ask if the user wants to continue.
#Assume that the user will enter valid data.
#Only continue if the user agrees to.
while True:
    posited_num = input('Please inset a positive integer: ')
    if posited_num.isdigit():
        if int(posited_num) > 0:
            break 
proceed = input('Do you want to continue? :')
if proceed.lower().startswith('y'):
    posited_num = int(posited_num)
    print()
    print('number  | squared | cubed')
    print('------  | ------- | -----')
    for i in range(1, posited_num + 1):
        i_squared = i ** 2
        i_cubed = i**3
        print(f'{i: 6}) | {i_squared: 7} | {i_cubed: 5}')




#5.) Convert given number grades into letter grades.

#Prompt the user for a numerical grade from 0 to 100.
#Display the corresponding letter grade.
#Prompt the user to continue.
#Assume that the user will enter valid integers for the grades.
#The application should only continue if the user agrees to.
#Grade Ranges:

A : 100 - 88
B : 87 - 80
C : 79 - 67
D : 66 - 60
F : 59 - 0

while True:
    user_grade = input("Please enter a number between 0 and 100")
    if user_grade.isdigit():
        user_grade = int(user_grade)
        if user_grade < 0 or user_grade > 100:
            continue
        break 

if user_grade in range(0,60):
    grade = 'F'
elif user_grade in range(61,67):
    grade = 'D'
elif user_grade in range(68,80):
    grade = 'C'
elif user_grade in range(81,88):
    grade = 'B'
else:
    grade = 'A'
print(grade)

#6.) Create a list of dictionaries where each dictionary represents a book that you have read. 
# Each dictionary in the list should have the keys title, author, and genre. 
# Loop through the list and print out information about each book.
#Prompt the user to enter a genre, then loop through your books list and print out the titles of 
# all the books in that genre.

bookshelf = [
    {'title': 'Cook Book for Birds',
    'author': 'Roger Sandoval',
    'genre': 'Comedy'},
    {'title': 'Chihuahuas in Sweaters',
    'author': 'Rogelio Sandoval',
    'genre': 'Non-fiction'},
    {'title': 'Los Conejos y Una Necia',
    'author': 'Rogelio G. Sandoval',
    'genre': 'Sci-Fi'},
      {'title': 'Haunting of Tortilla Chips',
    'author': 'Roggie Sandoval',
    'genre': 'Sci-Fi'},
]
for book in bookshelf:
    [print(key, ': ', book[key]) for key in book]
    print('----------')

select_genre = input('Please select a genre, and I will find you a book to your liking: ')

matches = []
for book in bookshelf:
    if book['genre'].lower() == select_genre.lower():
        matches.append(book['title'])
if matches == []:
    print('We must not have the same taste in books. Try again next time!')
else:
    print(f'This may be of interest to you, since you like {select_genre}:')
    [print(match) for match in matches]