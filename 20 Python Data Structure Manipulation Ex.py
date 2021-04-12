#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


students = [
    {
        "id": "100001",
        "student": "Ada Lovelace",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 91, 82, 71],
        "pets": [{"species": "horse", "age": 8}],
    },
    {
        "id": "100002",
        "student": "Thomas Bayes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [75, 73, 86, 100],
        "pets": [],
    },
    {
        "id": "100003",
        "student": "Marie Curie",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [70, 89, 69, 65],
        "pets": [{"species": "cat", "age": 0}],
    },
    {
        "id": "100004",
        "student": "Grace Hopper",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [73, 66, 83, 92],
        "pets": [{"species": "dog", "age": 4}, {"species": "cat", "age": 4}],
    },
    {
        "id": "100005",
        "student": "Alan Turing",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [78, 98, 85, 65],
        "pets": [
            {"species": "horse", "age": 6},
            {"species": "horse", "age": 7},
            {"species": "dog", "age": 5},
        ],
    },
    {
        "id": "100006",
        "student": "Rosalind Franklin",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [76, 70, 96, 81],
        "pets": [],
    },
    {
        "id": "100007",
        "student": "Elizabeth Blackwell",
        "coffee_preference": "dark",
        "course": "web development",
        "grades": [69, 94, 89, 86],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100008",
        "student": "Rene Descartes",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [87, 79, 90, 99],
        "pets": [{"species": "cat", "age": 10}, {"species": "cat", "age": 8}],
    },
    {
        "id": "100009",
        "student": "Ahmed Zewail",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [74, 99, 93, 89],
        "pets": [{"species": "cat", "age": 0}, {"species": "cat", "age": 0}],
    },
    {
        "id": "100010",
        "student": "Chien-Shiung Wu",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [82, 92, 91, 65],
        "pets": [{"species": "cat", "age": 8}],
    },
    {
        "id": "100011",
        "student": "William Sanford Nye",
        "coffee_preference": "dark",
        "course": "data science",
        "grades": [70, 92, 65, 99],
        "pets": [{"species": "cat", "age": 8}, {"species": "cat", "age": 5}],
    },
    {
        "id": "100012",
        "student": "Carl Sagan",
        "coffee_preference": "medium",
        "course": "data science",
        "grades": [100, 86, 91, 87],
        "pets": [{"species": "cat", "age": 10}],
    },
    {
        "id": "100013",
        "student": "Jane Goodall",
        "coffee_preference": "light",
        "course": "web development",
        "grades": [80, 70, 68, 98],
        "pets": [{"species": "horse", "age": 4}],
    },
    {
        "id": "100014",
        "student": "Richard Feynman",
        "coffee_preference": "medium",
        "course": "web development",
        "grades": [73, 99, 86, 98],
        "pets": [{"species": "dog", "age": 6}],
    },
]


# In[21]:


#1.)  How many students prefer light coffee? For each type of coffee roast?
    #light is 3, medium is 6, dark is 5. 
len(students)


# In[22]:



#2.)  How many students prefer light coffee? For each type of coffee roast?
    #light is 3, medium is 6, dark is 5. 
print(len([student for student in students if student['coffee_preference'] == 'light']))
print(len([student for student in students if student['coffee_preference'] == 'medium']))
print(len([student for student in students if student['coffee_preference'] == 'dark']))


# In[11]:


#3.) How many types of each pet are there?
print(set(sum([[pet['species'] for pet in student['pets']] for student in students], [])))

print("There are",[sum(len([pets['species'] for pets in student['pets'] if pets['species'] == 'cat']) for student in students)], "cats")
print("There are",[sum(len([pets['species'] for pets in student['pets'] if pets['species'] == 'dog']) for student in students)], "dogs")
print("There are",[sum(len([pets['species'] for pets in student['pets'] if pets['species'] == 'horse']) for student in students)], "horses")


# In[26]:


#4.) How many pets does each student have?
student = students[0]
student["pets"]
len(student["pets"])
number_of_pets =  len(student["pets"])
print(f"{student['student']} has {number_of_pets} pet(s)")

for student in students:
    number_of_pets =  len(student["pets"])
    print(f"{student['student']} has {number_of_pets} pet(s)") 


# In[12]:


#5.) What is each student's grade average?
[student['grades'] for student in students]
[sum(student['grades']) for student in students]
[(sum(student['grades'])) / (len(student['grades'])) for student in students]


# In[17]:


#6.) How many pets does each student have?
[len([pet for pet in student['pets']]) for student in students]


# In[30]:


#7.) How many students are in web development? data science?
print("The number of students in web development is ", len([student for student in students if student['course'] == 'web development']))
print("The number of students in data science is ", len([student for student in students if student['course'] == 'data science']))


# In[35]:


#8.) What is the average number of pets for students in web development?
sum([len(student['pets']) for student in students if student['course'] == 'web development']) / len([len(student['pets']) for student in students if student['course'] == 'web development'])
print("The average number of pets for students in web development is", sum([len(student['pets']) for student in students if student['course'] == 'web development']) / len([len(student['pets']) for student in students if student['course'] == 'web development']))


# In[46]:


#9.) What is the average pet age for students in data science?
pet_ages = sum(sum([[pet['age'] for pet in student['pets']] for student in students if student['course'] == 'data science'], []))
pet_ages

data_science_pets = len([[pet['age'] for pet in student['pets']] for student in students if student['course'] == 'data science'])
data_science_pets
pet_ages / data_science_pets

print("The average pet age for data science students is", pet_ages/data_science_pets)


# In[47]:


#10.) What is most frequent coffee preference for data science students?
data_coffee = [student['coffee_preference'] for student in students if student['course'] == 'data science']
data_coffee
max(set(list(zip([data_coffee.count(w) for w in data_coffee], data_coffee))))


# In[52]:


#11.) What is the least frequent coffee preference for web development students?
web_coffee = [student['coffee_preference'] for student in students if student['course'] == 'web development']
web_coffee
min(set(list(zip([web_coffee.count(w) for w in web_coffee], web_coffee))))
print("Least coffee preference for web development was", min(set(list(zip([web_coffee.count(w) for w in web_coffee], web_coffee)))))
min(set(list(zip([data_coffee.count(w) for w in data_coffee], data_coffee))))


# In[55]:


#12.) What is the average grade for students with at least 2 pets?
[(sum(student['grades'])) / (len(student['grades'])) for student in students if len(student['pets']) > 2]

print("The average grade for students with at least two pets is", [(sum(student['grades'])) / (len(student['grades'])) for student in students if len(student['pets']) > 2])


# In[57]:


#13.) How many students have 3 pets?
len([student for student in students if len(student['pets']) == 3])
print(len([student for student in students if len(student['pets']) == 3]), "student(s) have 3 pets")


# In[68]:


#14.) What is the average grade for students with 0 pets?
no_pets = [(sum(student['grades'])) / (len(student['grades'])) for student in students if len(student['pets']) == 0]

average_no_pets = (sum(no_pets)) / (len(no_pets))
print(f"Average grade for students with no pets is {average_no_pets}")


# In[77]:


#15.) What is the average grade for web development students? data science students?
web_dev = [(sum(student['grades'])) / (len(student['grades'])) for student in students if student['course'] == 'web development']

avg_web_dev = sum(web_dev) / len(web_dev)

data_science = [(sum(student['grades'])) / (len(student['grades'])) for student in students if student['course'] == 'data science']

avg_data_science = sum(data_science) / len(data_science)

print(f"The average grade for web dev students is {avg_web_dev}, and the average grade for data science students is {avg_data_science}")


# In[80]:


#16.) What is the average grade range (i.e. highest grade - lowest grade) for dark coffee drinkers?
coffee_grade_range = [max(student['grades']) - min(student['grades']) for student in students if student['coffee_preference'] == 'dark']

avg_coffee_grade_range = sum(coffee_grade_range) / len(coffee_grade_range)

print(f"The average grade range for dark coffee drinkers is {avg_coffee_grade_range}")


# In[83]:


#17.) What is the average number of pets for medium coffee drinkers?
medium_pets = [len(student['pets']) for student in students if student['coffee_preference'] == 'medium']

medium_pets_avg = sum(medium_pets) / len(medium_pets)

print(f"The average number of pets for medium coffee drinkers is {medium_pets_avg} ")


# In[85]:


#18.) What is the most common type of pet for web development students?
web_pet = [[pet['species'] for pet in student['pets']] for student in students if student['course'] == 'web development']
web_pet = sum(web_pet, [])

max(list(zip([web_pet.count(x) for x in web_pet], web_pet)))

print("Here is the number and most common type of pet for web dev students", max(list(zip([web_pet.count(x) for x in web_pet], web_pet))))


# In[88]:


#19.) Average Name Length
avg_name_length = sum([len(student['student']) for student in students]) / len([len(student['student']) for student in students])
print(f"The average name length for students is {avg_name_length}")


# In[91]:


#20.) What is the highest pet age for light coffee drinkers?
pet_ages = max(sum([[pet['age'] for pet in student['pets']] for student in students if student['coffee_preference'] == 'light'], []))
pet_ages

print(f"The oldest pet age for light coffee drinkers is {pet_ages}")


# In[ ]:




