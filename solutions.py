#1.) Write a function named isnegative. It should accept a number and return a boolean value based on whether the input is negative.

def isnegative(number): 
    return number<0

#2.) Write a function named count_evens. It should accept a list and return the number of even numbers in the list.
def count_evens(x):
    count = 0
    for ele in x:
        if ele%2 == 0:
            count+=1
    return count

#3.) Write a function named increment_odds. It should accept a list of numbers and return a new list with the odd numbers from the original list incremented.
def increment_odds(x):
    numbers = []
    for n in x:
        if n % 2 == 0:
            numbers.append(n)
        else:
            numbers.append(n+1)
    return numbers

#4.) Write a function named average. It should accept a list of numbers and return the mean of the numbers
def average(x):
    return sum(x)/len(x)

#5.) Create a function named name_to_dict. It should accept a string that is a first name and last name separated by a space, and return a dictionary with first_name and last_name keys.
def name_to_dict(name):
def name_to_dict(name):
    first_and_last = name.split()
    first = first_and_last[0]
    last = first_and_last[1]
    name = {
    "first_name": first,
    "last_name": last
}
    return name

#6.) Write a function named capitalize_names. It should accept a list of dictionaries where each dictionary represents a person and has keys first_name and last_name. It should return a list of dictionaries with each person's name capitalized.
def capitalize_names(names):
    first = 'first_name'[0].title()
    last = 'last_name'[-1].title()
    name = {
    "first": first,
    "last": last
}

    name = {
    "first": first[0],
    "last": last[-1]
}

    name["first"] = name["first"].title() 
    name["last"] = name["last"].title()
    return names

#7.) Write a function named count_vowels. It should accept a word and return a number that is the number of vowels in the given word. "y" should not count as a vowel.
def count_vowels(x):
    count = 0
    vowel = set ('aeiouAEIOU')
    for element in x:
        if element in vowel:
            count += 1
    return count

#8.) Write a function named analyze_word. It should accept a string that is a word and return a dictionary with information about the word: the total number of characters in the word, the original word, and the number of vowels in the word.
def analyze_word(x):
    number_of_characters = len(x)
    original_word = x
    number_of_vowels = count_vowels(x)
    word = {
    "word": original_word,
    "n_letters": number_of_characters,
    "n_vowels": number_of_vowels
}
    return word