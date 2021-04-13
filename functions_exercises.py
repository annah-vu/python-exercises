#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[8]:


lst = [0,1,2,5]
def cumulative_sum(numbers):
    for n in range(numbers):
        lst.append(numbers)
sum(lst) 
        


# In[9]:


sum([1,2,3])


# In[3]:


#1.) Define a function named is_two. It should accept one input and return True if the passed input is either the number or the string 2, False otherwise.
def is_two(n):
    if n == 2 or n == '2':
        return True
    else:
        return False
print(is_two(2))


# In[10]:


# 2.) Define a function named is_vowel. It should return True if the passed string is a vowel, False otherwise.
def is_vowel(letter):
    vowel = set('AEIOUaeiou')
    if letter in vowel:
        return True
    else: 
        return False
print(is_vowel('e'))


# In[15]:


#3.) Define a function named is_consonant. It should return True if the passed string is a consonant, False otherwise. Use your is_vowel function to accomplish this.
def is_consonant(letter):
    if is_vowel(letter) == False:
        return True
    else:
        return False
print(is_consonant('h'))


# In[19]:


#4.) Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
def capitalize_consonant(string):
    if is_consonant(string[0]) == True:
        return string.capitalize()
    else:
        return string        
print(capitalize_consonant('cat'))


# In[26]:


#5.) Define a function named calculate_tip. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
def calculate_tip(tip_percent, bill_total):
    if tip_percent < 0 or tip_percent >= 1:
        return print(f'{tip_percent} is invalid.')
    else:
        return tip_percent * bill_total
print(calculate_tip(.20, 100))


# In[35]:


#6.) Define a function named apply_discount. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
def apply_discount(og_price, disc_perc):
    if disc_perc < 0 or disc_perc > 1:
        return print(f'{disc_perc} is not in percentage form')
    else:
        return og_price - (og_price * disc_perc)
apply_discount(50, .10)


# In[43]:


#7.)Define a function named handle_commas. It should accept a string that is a number that contains commas in it as input, and return a number as output.
def handle_commas(num):
    num = num.replace(',','')
    return int(num)
print(handle_commas('3,,,,4,'))


# In[49]:


#8.) Define a function named get_letter_grade. It should accept a number and return the letter grade associated with that number (A-F).
def get_letter_grade(num):
    if num > 89:
        return (f'{num} is an A')
    elif num > 79:
        return (f'{num} is a B')
    elif num > 69:
        return (f'{num} is a C')
    elif num > 59:
        return (f'{num} is a D')
    else:
        return (f'{num} is an F')
print(get_letter_grade(100))


# In[54]:


#9.) Define a function named remove_vowels that accepts a string and returns a string with all the vowels removed.
def remove_vowels(string):
    newstring = string
    vowels = ('a', 'e', 'i', 'o', 'u')
    for x in string.lower():
        if x in vowels:
            newstring = newstring.replace (x, "")
    return newstring
print(remove_vowels('i love birds'))


# In[55]:


#10.) Define a function named normalize_name. It should accept a string and return a valid python identifier, that is:
#anything that is not a valid python identifier should be removed
#leading and trailing whitespace should be removed
#everything should be lowercase
#spaces should be replaced with underscores

def normalize_name(string):
    string = string.lower()
    string = string.strip()
    string = string.replace(" ", "_")
    for i in string:
        if i.isdigit() == True or i.isalpha() == True or i == "_":
            continue
        else:
            string = string.replace(i, "")
    return string
    
print(normalize_name(' My name is ROWDY!!!@@  '))


# In[59]:


#11.) Write a function named cumulative_sum that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
def cumulative_sum(list_of_numbers):
    new_list = []
    length = len(lists)
    new_list = [sum(lists[0:x:1]) for x in range(0, length+1)]
    return new_list[1:]

lists = [10, 20, 30, 40, 50]
print (cumulative_sum(lists))


# In[ ]:
# or
def cumulative_sum(numbers):
    new_numbers = []
    sums = []
    for num in numbers:
        new_numbers.append(num)
        sums.append(sum(new_numbers))
    return sums
cumulative_sum([10,20,30,40,50])



