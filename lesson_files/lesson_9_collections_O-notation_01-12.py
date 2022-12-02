#!/usr/bin/env python
# coding: utf-8

# ### Lesson 9. Collections/O-notation/Style of Coding. Date: 01.12.22
# **Topics**:
# >    1. DefaultDict
# >    2. Tutple/namedtuple/Namedtuple
# >    3. Generators
# >    4. *Args, *\*Kwargs
# >    5. Flake8/Git
# >    6. Algorithm
# >    7. Big O notation
# 
# **Materials** :
# > 1. [Default dict](https://realpython.com/python-defaultdict/)
# > 2. [DefaultDict doc](https://docs.python.org/3/library/collections.html)
# > 3. [namedtuple](https://docs.python.org/3/library/collections.html#collections.namedtuple)
# > 4. [O - notation](https://medium.com/fintechexplained/time-complexities-of-python-data-structures-ddb7503790ef)
# > 5. [Git english](https://www.vogella.com/tutorials/Git/article.html)
# > 6. [Git quick start](https://github.com/andreiled/mipt-cs-4sem/wiki/Пошаговая-инструкция-по-работе-с-git-и-github-для-студентов)
# > 7. [Flake8](https://flake8.pycqa.org/en/latest/)
# 
# 

# In[13]:


from collections import defaultdict


# In[213]:


standart_dict = {
    'Paris': 'France',
    'Kyiv': 'Ukraine',
    'Berlin': 'Germany',
}


# In[214]:


standart_dict['Paris']


# In[215]:


standart_dict['Mexico'] # Що поверне код?


# In[217]:


if 'Mexico' in standart_dict.keys():
    standart_dict['Mexico'] += 1
else:
     standart_dict['Mexico'] = 0
print(standart_dict)


# In[77]:


r = defaultdict(int)


# In[218]:


int()


# In[219]:


r['Mexico']


# In[220]:


r_with_list = defaultdict(list)  # Вказуємо тип по замовучанню                         


# In[221]:


r_with_list['Pattern']


# In[93]:


r_with_list['Pattern1'] = [1,2,3]


# In[222]:


r_with_list


# In[108]:


def create_value():
    return 'No value input'


# In[110]:


r_with_def_func = defaultdict(create_value)


# In[111]:


r_with_def_func[0]


# In[223]:


r_with_def_func


# ### Compehension dict
# dictionary = {key: value for vars in iterable} - how to create \
# **key** - first postion argument, will be a key for dict(only unique hash value) \
# **:** - operator to create pair \
# **value**  - value than we match with key \

# In[113]:


dict_ = dict()
for i in range(15):
    dict_[i] = i ** 2
print(dict_)


# In[120]:


dict_ = {i: i ** 2 for i in range(15) if i % 2 == 0} # Create compehension with comparion
print(dict_)


# In[121]:


dict_ = {i: (i ** 2 if i % 2 == 0 else i ** 3) for i in range(15)} # With two var of keys
print(dict_)


# In[ ]:





# ### Zip - function 
# zip - key_word  \
# zip = iter1, iter2, iter3 ... iterN

# In[224]:


a = [1,2,3,4,5]
b = [100, 200, 300, 400, 500, 600]

res = list(zip(a, b))


# In[ ]:





# In[225]:


for i in zip(a,b):
    print(i, type(i))


# In[131]:


dict_key = dict()
for i in zip(a, b):
    dict_key[i[0]] = i[1]
print(dict_key)


# In[133]:


dict_key = dict()
for key, value in zip(a,b):
    dict_key[key] = value
print(dict_key)


# In[ ]:





# #### Unpacking operator
# **Args(*)** - unpacking operator \
# **Kwargs(**)** - unpacking operator for dictionary

# In[227]:


a, b, c = [True, 'True', 15] # Try add more value
print(a,b,c)


# In[228]:


a, *b, c = [True, 'True', 15, 16,17]
print(a, b, c)


# In[147]:


a, *b, c = [True, 'True', 15, 16,17]
print(a, b, c)


# In[151]:


*a, b, c = [True, 'True', 15, 16,17]
print(a, b, c)


# In[232]:


a, b, *c = (True, 'True', 15, 16,17)
print(a, b, c)


# In[246]:


b, *args, a  = 1,2,3, 4
print(*args, a, b)


# In[243]:


def add_number(*args):
    print(type(args), args)
    sum_ = 0
    for i in args:
        sum_ += 1
    return sum_


# In[ ]:


tupple = 1,2


# In[244]:


print(add_number([1,2,3]), add_number(1,2,3,4))


# In[ ]:





# In[186]:


def create_dict(**kwargs):
    print(kwargs, type(kwargs))
    


# In[189]:


create_dict(a = 4, b = 5, c = 6)


# In[187]:


# *kwargs
def function_with_kwargs(argument1, *args, **kwargs):
    print(f'argument1: {argument1}')
    print(f'args: {args}')
    print(f'kwargs: {kwargs}')


# In[188]:


function_with_kwargs(1, 2, 3, argument4=4, argument5=5)


# In[ ]:





# In[ ]:


# Enumerate - return tuple with elements(index, value)


# In[204]:


a = [1,2,3,4,5,6]
for i in enumerate(a):
    print(i)


# In[248]:


a = [i ** 2 for i in range(1,8)]
for i in range(0, len(a)):
    print(f'Index: {i} Value: {a[i]}')


# In[247]:


a = [i ** 2 for i in range(1,8)]
for counter, value in enumerate(a, start = 1):
    print(f'Counter : {counter} Value: {value}')


# In[ ]:





# In[18]:


from collections import namedtuple # імпорт покращеного tutple


# In[19]:


standart_tutple = 1,2,3,4, '5'


# In[24]:


print(standart_tutple[0], standart_tutple[-1])
print(standart_tutple ,type(standart_tutple), standart_tutple.__sizeof__())


# In[ ]:





# In[ ]:





# In[253]:


Car = namedtuple('Car1', ['mark', 'color', 'size_of_engines', 'type_of_fuel', 'year'])
Car


# In[257]:


jaguar = Car(mark = 'Jaguar Range Rover', color = 'black', size_of_engines = 2.5, type_of_fuel  = 'petrol', year = 2008)


# In[258]:


jaguar.mark # Отримуємо доступ до елементів по імені 


# In[ ]:





# In[249]:


jaguar[0]


# In[73]:


Person = namedtuple("Person", "name children")
john = Person("John Doe", ["Timmy", "Jimmy"])


# In[75]:


john.children.append('New name')


# In[259]:


john.children


# In[260]:


john.children.append("Tina")
john


# In[ ]:


jaguar[0] # Що поверне код?


# In[261]:


from typing import NamedTuple # імпорт tuple, в якому можна вказувати анотацію типів


# In[56]:


class Car_Named(NamedTuple): # Створення структури namedtuple
    mark : str
    color : str
    size_of_engines: float
    type_of_fuel: str
    year: int


# In[54]:


porsche = Car_Named(mark = 'Porsche', color = 'red', 
                    size_of_engines = 3.5,  type_of_fuel = 'patrol', 
                   year = 2015)


# In[267]:


porsche[-1]


# In[262]:


porsche.color


# In[264]:


porsche.size_of_engines


# In[50]:


porsche[0] # Що повернє код?


# In[ ]:





# Task 1. Вводятся целые числа. Необходимо четные добавлять в начало списка, а нечетные - в конец.

# In[ ]:





# Task 2. Вводится строка. Необходимо определить в ней проценты прописных(больших) и строчных (малых) букв.

# In[ ]:





# Task 3. Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
# 
# 
# Example 1:
# 
# Input: nums = [1,3,5,6], target = 5
# Output: 2
# Example 2:
# 
# Input: nums = [1,3,5,6], target = 2
# Output: 1
# Example 3:
# 
# Input: nums = [1,3,5,6], target = 7
# Output: 4
#  

# In[ ]:





# ** Add example
# Task 4. Write an efficient function that checks whether any permutation of an input string is a palindrome. Note that the function is not a palindrome check.
# 
# Examples:
# 
# "civic" should return True \
# "ivicc" should return True  (because “civic” is a permutation of “ivicc”) \
# "civil" should return False \
# "livci" should return False
# 

# In[ ]:





# ### How to pick right data structure. 

# To pick right data structure, we need to understand what data we will store there and operations that we will perform on it. To optimize the program, we should understand time that will take some operations for each data structure.

# **Complexity** - time complexity is a function describing the amount of time an algorithm takes in terms of the amount of input to the algorithm. "Time" can mean the number of memory accesses performed, the number of comparisons between integers, the number of times some inner loop is executed, or some other natural unit related to the amount of real time the algorithm will take.

# In[ ]:





# ## How list works

# What happens when you create a list
# 
# ```python
# my_list = []
# ```
# 
# Python allocates constant amount of space event for empty list, amount of the allocated space is might be bigger than size of the list. Also, python saves save the size of the element to have quick access to this value.
# 
# In complexity terms we call it constant time - **O(1)**. It means that time of execution doesn`t depend on the size of the list or any other parameter.
# 
# 

# In[ ]:





# ### Indexing
# 
# To find an element python need constant time because we know where is the first cell, size of the cell and index of the element. Due to all this things, we can multiply cell_size on index and we will find element that we need. Complexity is **O(1)**. \
# **Question** - how can we know an offset if list contains different data types?

# ### Append
# 
# 1. Easy case - find empty space in the memory that was allocated for the list and add the element for the first empty cell. After that, you should increase the size of the list.
# 2. Hard case - you don`t have empty space in the memory, you need to allocate more memory for the list.
#     1. You should allocate more memory for the list. Python use next pattern: 0, 4, 8, 16, 25, 35, 46, 58, 72, 88, … After Python adds empty cells, it copies all the elements from the old list to the new list. At the end it should change pointer to the new list. After that steps we jump to the first case. 
# 
# In this case we understand that python need more time to execute this operation, but it also performs in a constant time - **O(1)** because it doesn`t depend on the size of the list. 

# In[ ]:





# ### Insert
# 
# 1. Let`s take a look at the code:
# 
# ```python
# my_list = [1, 2, 3]
# my_list.insert(3, 4)
# ``` 
# 
# To execute this operation Python should add 4 at the end of list if list has empty cells. If not, we should allocate additional memory for the list like we did it in the previous case. 
# Complexity - **O(1)**. 
# 
# 2. Also, you might to insert element at the beginning of the list: 
# 
# ```python
# my_list = [1, 2, 3]
# my_list.insert(0, 4)
# ``` 
# 
# To do that Python needs shift all elements in the list to the right. After that we can insert element at the beginning of the list. Complexity - **O(n)**. Here complexity depends from amount of elements in the list.
#  

# ### Pop
# 
# Here we also have two cases:
# 
# 1. Pop element at the end of the list.
# 
# Python should remove element from cell and shrink the list if necessary. Complexity - **O(1)**.
# 
# 2. Pop element at the beginning of the list (in the middle).
# 
# Here situation is a bit harder. Python should remove element from cell and shift all elements to the left. Complexity - **O(n)**.

# In[ ]:





# ## Tuple
# 
# Tuple is a bit easier to understand. It is a list that can`t be changed. So here is the same complexity for same operation with list. 

# In[ ]:





# In[ ]:





# In[ ]:





# ## Dictionary
# 
# ### Hash function
# 
# What is a Hash Function? 
# 
# A function that converts a given big phone number to a small practical integer value. The mapped integer value is used as an index in the hash table. In simple terms, a hash function maps a big number or string to a small integer that can be used as the index in the hash table. 
# 
# **Example in security (md5, sha/2)**
# 
# What is meant by Good Hash Function? 
# 
# A good hash function should have the following properties: 
# 
#     1. Efficiently computable.
#     
#     2. Should uniformly distribute the keys (Each table position equally likely for each key)
# 
#     3. Should return the same output for the same input.
# 
# For example: For phone numbers, a bad hash function is to take the first three digits. A better function is considered the last three digits. Please note that this may not be the best hash function. There may be better ways. 
# 

# In[10]:


a = 3.14


# In[12]:


hash(3.14) == hash(a)


# In[8]:





# ### Fibonacci 
# 
# ```python
# def fibonacci(n: int) -> int:
#     if n <= 1:
#         return 1
#     
#     return fibonacci(n - 2) + fibonacci(n - 1);
# ```
# 
# ![fib](https://i.stack.imgur.com/6hD41.png)
# 
# Complexity - O(2 ^ n)

# In[193]:


# Quick sort

def quick_sort(list_):
    if len(list_) < 2:
        return list_
    else:
        pivot = list_[0]
        less = [i for i in list_[1:] if i <= pivot]
        greater = [i for i in list_[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

#    [4, 5, 6, 2, 1, 3, 7]
#        /     |     \
# [2, 1, 3] + [4] + [5, 6, 7]
# /   |   \    |     /   |   \
# [1] [2] [3]  |   []  [5]  [6, 7]
# [1] [2] [3]  |          /   |  \
#              |      []  +  [6] + [7]
# [1, 2, 3]    |   [5, 6, 7]
#    [1, 2, 3, 4, 5, 6, 7]

# Here is the complexity:

# 1. Find list of smaller elements -> O(n)
# 2. Find list of greater elements -> O(n)



# ### Practice
# 
# **You have 100 cats.**
# 
# One day you decide to arrange all your cats in a giant circle. Initially, none of your cats have any hats on. You walk around the circle 100 times, always starting at the same spot, with the first cat (cat # 1). Every time you stop at a cat, you either put a hat on it if it doesn’t have one on, or you take its hat off if it has one on.
# 1. The first round, you stop at every cat, placing a hat on each one.
# 2. The second round, you only stop at every second cat (#2, #4, #6, #8, etc.).
# 3. The third round, you only stop at every third cat(#3, #6, #9, #12, etc.).
# 4. You continue this process until you’ve made 100 rounds around the cats (e.g., you only visit the 100th cat).
# Write a program that simply outputs which cats have hats at the end.
# 
# Optional: Make function that can calculate hat with any amount of rounds and cats.
# 
# Here you should write an algorithm, after that, try to make pseudo code. Only after that start to work. Code is simple here, but you might struggle with algorithm. Therefore don`t try to write a code from the first attempt. 
# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




