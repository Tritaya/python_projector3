#!/usr/bin/env python
# coding: utf-8

# ### Lesson 6. Tuple and operation. List and operation. 15.11 - 19.11
# >    **Topic**: \
# >        1. Tuple \
# >        2. Operation with tuple \
# >        3. Tuple function \
# >        4. List/opearation with list \
# >        5. List function
# 
# >    **Materials**: \
# >        1. [Lists w3schools](https://www.w3schools.com/python/python_arrays.asp) \
# >        2. [More lists in w3school](https://www.w3schools.com/python/python_lists.asp) \
# >        3. [Realpython lits](https://realpython.com/python-scope-legb-rule/) \
# >        4. [Realpython tuples](https://realpython.com/python-lists-tuples/) \
# >        5. [Learnpython](https://www.learnpython.org) - find lists/tuples \
# >        6. [Exceptions](https://realpython.com/python-exceptions/)
#        

# ### Scope

# In[ ]:


# exchange money / weather app / twiter - парсер cloud тег / machine learning / try - except* /


# In[1]:


x = 3

print(x)

x = 5
print(x)


# In[2]:


x = 5

def function():
    x = 2
    print(f'Inside function x = {x}')
    
function()
print(f'Outside function x = {x}')


# In[4]:


x = 2

def outer_func():
    y = 3
    def inner_func():
        j = 5
        return x + y + j
    
    return inner_func()

result = outer_func()
print(f'Result is {result}')


# In[ ]:





# In[ ]:





# ### LEGB rule
# 
# **Local (L)**: The local, or current, scope. This could be the body of a function or the top-level scope of a script. It always represents the scope that the Python interpreter is currently working in.
# 
# **Enclosing (E)**: The enclosing scope. This is the scope one level up from the local scope. If the local scope is an inner function, the enclos- ing scope is the scope of the outer function. If the scope is a top-level function, the enclosing scope is the same as the global scope.
# 
# **Global (G)**: The global scope, which is the top-most scope in the script. This contains all of the names defined in the script that are not contained in a function body.
# 
# **Built-in (B)**: The built-in scope contains all of the names, such as keywords, that are built-in to Python. Functions such as round() and abs() are in the built-in scope. Anything that you can use without first defining yourself is contained in the built-in scope.

# In[ ]:





# In[7]:





# ## Practice block 1:
# 
# 1. Create an outer function that will accept two parameters, a and b
# 2. Create an inner function inside an outer function that will calculate the addition of a and b
# 3. At last, an outer function will add 5 into addition and return it

# In[ ]:





# In[67]:


# Перевірка з презентації
a = [1,2,3,[4,5,[2,3,4],6,7],6,7]
print(f'{a[3][2][0]} \n{a[3]} {a[10]}')


# In[3]:





# In[8]:


total = 0
def add_to_total(n): # Що поверне код?
    total = total + n
print(add_to_total(5))


# In[9]:


total = 0
def add_to_total(n):
    total1 = total + n

add_to_total(5)
print(total)


# In[11]:


total = 0
def add_to_total(n):
    global total # Ключове слово для глобальний, bad style 
    total = total + n

add_to_total(5)
add_to_total(5)
print(total)


# In[12]:


total = 0
def add_to_total(base_value: int, n: int) -> int:
    return base_value + n # Best style

total = add_to_total(total, 5)
print(total)


# ### Task 1
# A perfect number is a number in which the sum of its divisors (excluding itself) are equal to itself.
# 
# Write a function that can verify if the given integer n is a perfect number, and return True if it is, or return False if not.
# 
# Examples
# 
# n = 28 has the following divisors: 1, 2, 4, 7, 14, 28
# 
# 1 + 2 + 4 + 7 + 14 = 28 therefore 28 is a perfect number, so you should return True
# 
# Another example:
# 
# n = 25 has the following divisors: 1, 5, 25
# 
# 1 + 5 = 6 therefore 25 is not a perfect number, so you should return False
# 

# In[ ]:


# Step 1: %, ==, +, bool
# Step 2: while/for, range 
# Step 3: def, return


# In[41]:


counter = 1
n = 28
s = 0
while counter != n - 1:
    if n % counter == 0:
        print(counter)
        s += counter
    counter += 1
print(n == s)


# ## Practice block 2
# 
# 
# 1. Write a program that asks user to enter an integer and convert it to int. If the user enters something that is not an integer, program should catch an error and ask the user to enter an integer again. if user inputs an integer, program should print this number and quit w/o any error.
# 2. Write a program that asks the user to input a string and an integer n. Then display the character at index n in the string. You should handle an error properly and display proper error message.

# In[17]:


### Try/Except block


# In[118]:


int('q')


# In[119]:


int('--3.14')


# In[120]:


int(--4.15)


# In[121]:


float('a')


# In[122]:


1 / 0


# In[124]:


number = int(input("Enter an integer: "))


# In[125]:


try:
    number = int(input("Enter an integer: "))
except ValueError:
    print("That was not an integer")
    number = 10

print(number)


# In[127]:


1 / 0


# In[ ]:





# In[137]:


def divide(num1, num2):
    try:
        print(num1 / num2)
    except ( ZeroDivisionError) as e:
        print('Founded an error:', e)
    except:
        print('No found error')

divide(1, 'd')


# In[141]:


# Catch all exceptions
try:
    number = int(input("Enter an integer: "))
except ValueError as e:
    number = 10
    print(f'Your input: {number}')
except (TypeError, ZeroDivisionError) as e:
    print("Something bad happened!", e)
except Exception : 
    print('except Exception', Exception)
    
print('Finally')


# In[142]:


x = -3


# In[1]:


# raise the exception manually
if x < 0:
    # pass
    raise ValueError("Sorry, no numbers below zero")
    


# In[40]:


#### Module random


# In[29]:


import random as rd # дозволяє працювати з псевдорандом


# In[30]:


rd.randint(4, 10) # Дозволяє повертати в діапозоні числа,  start: end


# In[ ]:





# ## Practice block 3:
# 
# 1. Write a function that simulate a dice roll and returns the result from 1 to 6.
# 2. Write a function that simulate 10_000 rolls and returns the number of times that the dice roll for each value
# 3. Simulate an election for two candidates. Program should take amount of regions and rating for 1st candidate in each region (in percentage). Program should run election in every region. In every region, program should ask 10 000 voters. Candidate count as a winner if he gains more than 50% of all votes. Program should print the result of the election for each region and the winner
# 
#     Example:
# 
#     Enter number of regions: 2 
# 
#     Enter rating for 1st candidate in each region: 34, 56
# 
#     Region 1: 3456 votes for 1st candidate, 6544 votes for 2nd candidate
# 
#     Region 2: 5623 votes for 1st candidate, 4356 votes for 2nd candidate
# 
#     Result: 2nd candidate won with 10900 votes and 54.5% of all votes
# 

# In[46]:


### Tuple


# In[ ]:





# In[85]:


tuple_example = ((1, 2, 3), 4, 5)
type(tuple_example)


# In[86]:


print(tuple_example)


# In[77]:


tuple_second = (1, '2', True, [1,2,3])
tuple_second


# In[78]:


empty_tuple = ()
empty_tuple


# In[79]:


t = (1) # Що поверне?
type(t)


# In[82]:


t = (1,)
type(t)


# In[83]:


t = 1,
type(t)


# In[84]:


t2 = (1, 2), 2, (3, 4)
t2


# In[ ]:


t = ()
type(t)


# In[ ]:


_tuple = tuple()
type(_tuple)


# In[87]:


len(tuple_example)


# In[92]:


print(tuple_example)
print(tuple_example[2])


# In[101]:


print(tuple_example[1:3])


# In[56]:


tuple_example


# In[95]:


tuple_example[2] = 10


# In[ ]:


tuple2 = (1,2,3,4,5)


# In[114]:


tutple_1 =  ('september', 'october', 'november')

#long_month = (1, 3, 5, 7, 8)
#if month in long_month:
#    pass
    # do something


# In[117]:


print(tuple_example)
for i in tuple_example:
    print(j)


# In[ ]:





# ## Practice block 4
# 
# 1. Create a tuple with your first name, last name, and age.
# 2. Print your last name using indexing.
# 3. Create three variables in one line that extracted from tuple that you created in step 1.
# 4. Print your name letter by letter from this tuple
# 5. Create a new tuple that contains all info from the first tuple but remove first letter from all strings
# 6. Create a tuple with two values. First one is (1, 2), second one is (3, 4).
# 7. Create a program that calculates the sum of all values in the tuple and print it to the console.

# In[ ]:





# In[ ]:





# In[ ]:




