fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']

#Exercise 1 - rewrite the above example code using list comprehension syntax.
#Make a variable named uppercased_fruits to hold the output of the list comprehension.
#Output should be ['MANGO', 'KIWI', etc...]

uppercased_fruits = [fruit.upper() for fruit in fruits]
print(uppercased_fruits)

# Exercise 2 - create a variable named capitalized_fruits 
# and use list comprehension syntax to produce output like 
# ['Mango', 'Kiwi', 'Strawberry', etc...]

capitalized_fruits = [fruit.title() for fruit in fruits]
print(capitalized_fruits)

 #Exercise 3 - Use a list comprehension to make a variable named 
 #fruits_with_more_than_two_vowels. 
 #Hint: You'll need a way to check if something is a vowel.

def count_vowels(x):
    count = 0
    vowel = set ('aeiouAEIOU')
    for element in x:
        if element in vowel:
            count += 1
    return count

fruits_with_more_than_two_vowels = [fruit for fruit in fruits if count_vowels(fruit) > 2]
 
 # Exercise 4 - make a variable named fruits_with_only_two_vowels. 
 # The result should be ['mango', 'kiwi', 'strawberry']
 def count_vowels(x):
    count = 0
    vowel = set ('aeiouAEIOU')
    for element in x:
        if element in vowel:
            count += 1
    return count

fruits_with_only_two_vowels = [fruit for fruit in fruits if count_vowels(fruit) = 2]

# Exercise 5 - make a list that contains each fruit with more than 5 characters
[fruit for fruit in fruits if len(fruit) > 5]

#Exercise 6 - make a list that contains each fruit with exactly 5 characters
[fruit for fruit in fruits if len(fruit) == 5]

#Exercise 7 - Make a list that contains fruits that have less than 5 characters
[fruit for fruit in fruits if len(fruit) < 5]

#Exercise 8 - Make a list containing the number of characters in each fruit.
 Output would be [5, 4, 10, etc... ]
[len(fruit) for fruit in fruits]

# Exercise 9 - Make a variable named fruits_with_letter_a that contains 
# a list of only the fruits that contain the letter "a"
def count_a(x):
    count = 0
    letter_a = set ('Aa')
    for element in x:
        if element in letter_a:
            count += 1
    return count
fruits_with_letter_a = [fruit for fruit in fruits if count_a(fruit) >= 1]
print(fruits_with_letter_a)

# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 
even_numbers = [number for number in numbers if number % 2 == 0]

# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers
odd_numbers = [number for number in numbers if number % 2 != 0]

# Exercise 12 - Make a variable named positive_numbers that holds only the 
# positive numbers
positive_numbers = [number for number in numbers if number > 0]

# Exercise 13 - Make a variable named negative_numbers that holds only the 
# negative numbers
negative_numbers = [number for number in numbers if number < 0]

# Exercise 14 - use a list comprehension w/ a conditional in order to produce 
# a list of numbers with 2 or more numerals
[number for number in numbers if number >= 10 or num <= -10]

# Exercise 15 - Make a variable named numbers_squared that contains the numbers 
# list with each element squared. Output is [4, 9, 16, etc...]
numbers_squared = [number ** 2 for number in numbers]

# Exercise 16 - Make a variable named odd_negative_numbers that contains only the
#  numbers that are both odd and negative.
odd_negative_numbers = [number for number in numbers if number % 2 != 0 and number < 0]

# Exercise 17 - Make a variable named numbers_plus_5. 
# In it, return a list containing each number plus five. 
numbers_plus_5 = [number + 5 for number in numbers]

#Prime Number Bonus
def isprime(num):
    if num >=2:
        for n in range(2,num):
            if not (num % n == 0):
                return false 
    else: 
        return True 



#20 Python Data Structure Manipulation Exercises

#1.) How many students are there? 
# There are 14 students. 
 len(students)

# How many students prefer light coffee? For each type of coffee roast?
    #light is 3, medium is 6, dark is 5. 
len([student for student in students if student['coffee_preference'] == 'light'])
len([student for student in students if student['coffee_preference'] == 'medium'])
len([student for student in students if student['coffee_preference'] == 'dark'])

#How many types of each pet are there?

How many grades does each student have? Do they all have the same number of grades?
What is each student's grade average?
How many pets does each student have?
How many students are in web development? data science?
What is the average number of pets for students in web development?
What is the average pet age for students in data science?
What is most frequent coffee preference for data science students?
What is the least frequent coffee preference for web development students?
What is the average grade for students with at least 2 pets?
How many students have 3 pets?
What is the average grade for students with 0 pets?
What is the average grade for web development students? data science students?
What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?
What is the average number of pets for medium coffee drinkers?
What is the most common type of pet for web development students?
What is the average name length?
What is the highest pet age for light coffee drinkers?