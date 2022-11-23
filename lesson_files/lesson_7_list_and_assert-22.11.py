#!/usr/bin/env python
# coding: utf-8

# ### Lesson 7. Assert, Lists, Function. 22.11 
# > **Topic**: \
# > **1.** Assert \
# > **2.** Lists and function \
# > **3.** Practise 
# 
# > **Materials:**
# > 1. [Asserts](https://realpython.com/python-assert-statement/)
# > 2. [Lists and tutple](https://realpython.com/python-lists-tuples/)
# > 3. [Lists](https://pyneng.readthedocs.io/ru/latest/book/04_data_structures/lists.html)
# > 4. [Try to solve simple task](https://www.codewars.com/dashboard)
# 

# Контрольні запитання: 
# >    **1.** Різниця Tutple/List \
# >    **2.** Що виведе наступний код: tuple_ = ('tuple_element') \
# >    **3.** Навіщо існують різни типи даних? \
# >    **4.** Що таке колекція? 

# In[ ]:





# In[ ]:


### Assert - оператор перевірки, повертає True/False якщо тест пройшов або ні


# In[171]:


# assert умова яку хочете перевірити
a = 4
assert a == 4


# In[4]:


a = 2 
assert a == 4


# In[172]:


a = 2
assert a == 4, f'Wrong a value, we wait 4 return {a}'


# In[174]:


assert len((1, 2, 3)) == 3, f'Wrong len'


# In[ ]:





# In[181]:


def add_value(a:int, b: int) -> int:
    return a + b


# In[184]:


assert add_value(5, 5) == 10
# assert add_value('a', 'b') == 'Wrong value'
assert add_value('str', 'plus') == 'strplus'
assert add_value(1.0, 5) == 6.0


# In[ ]:





# In[195]:


def enrich_tutor_details(name: str, array: list):
    name += " is a great tutor"
    array.append('Spanish')
    return name, array
    

def test_enrich_tutor_details():
    username = 'John'
    languages = ['English']
    username, languages = enrich_tutor_details(username, languages)
    assert username == 'John is a great tutor'
    assert languages == ['English', 'Spanish']


# In[196]:


test_enrich_tutor_details()


# In[ ]:





# In[ ]:





# #### Lists 
# 1. Дефініція?
# 2. Доступ до елементів?
# 3. Які типи може зберігати?

# In[197]:


numbers = ['first',2, '3', 4, '5', '8', -1]


# In[198]:


_tuple = (1, 2, 3)
print(type(_tuple), _tuple)
_list = list(_tuple) # Перетворення в list
print(_list)


# In[199]:


list('a,b,c') # Що поверне код?


# In[200]:


print('a,b,c'.split(','))


# In[ ]:


# Slice [start: end: step] can use neg index 


# In[203]:


numbers = [1,2, 3, 4, 5]
numbers[1:3:2] 


# In[204]:


print(2 in numbers)
print(3 in numbers)


# In[205]:


print(numbers)
numbers[1] = 'second' # якщо хочемо змінити значення, вказуємо індекс і нове значення 
print(numbers)


# In[206]:


print(numbers)
numbers[1:3] = 5, 10 # Зміна за допомогою Slice
print(numbers)


# In[207]:


dir(list) # dir - повертае доступні методи 


# In[212]:





# In[216]:


print(numbers)
numbers = numbers + [3] # Добавляємо один елемент 
print(numbers)


# In[218]:


print(numbers)

numbers.append([1,2]) # Добавляємо в кінець один елемент 

numbers.append(1) 
print(numbers)


# In[224]:


numbers.index(1, 5, 9)


# ### Task 1. 
# Створити два списка, number, square, користувач вводить перший список(з консолі),
# після цього ми повертаемо квадрат до кожного числа. 
# * Обгорнути все в функцію з анотацією
# * Написати функцію з тестами
# * Використати try/except \
# Example: 
# [1,2,3,4,5] -> [1, 4, 9, 16, 25] 

# In[67]:


### Домашка - 
def square_arr(arr: list) -> list:
    pass


# In[ ]:





# ### Task 2
# In this task you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.
# 
# Example:  \
# filter_list([1,2,'a','b']) == [1,2] \
# filter_list([1,'a','b',0,15]) == [1,0,15] \
# filter_list([1,2,'aasf','1','123',123]) == [1,2,123] 
# 

# In[238]:


# Домашка
def filter_list(arr: list) -> list:
    pass


# In[255]:





# In[ ]:





# In[253]:


def test_filter_list(): 
    assert filter_list([1,2,'a','b']) == [1,2] , f'You return wrong value, need = [1,2]' 
    assert filter_list([1,'a','b',0,15]) == [1,0,15]
    assert filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
    assert filter_list(['403', 'i', 174, 'G', '396', 572, 644, '72', '311']) ==  [174, 572, 644]
    
    assert filter_list([231, '127', 'lmAY^', '\\E^', 69, 887, 959, 679, 570, 'j', 735, 132, 846, 'QfT', '457']) \
    == [231, 69, 887, 959, 679, 570, 735, 132, 846]
    assert filter_list([969, 'yQ8_J', '491', 465, '647', '228', '431']) == [969, 465]


# In[ ]:





# In[256]:


test_filter_list()


# In[ ]:





# In[257]:


print(numbers)
numbers.insert(1, 'half') # Вставити елемент на позицію 

print(numbers)


# In[258]:


numbers = [i for i in range(1, 6)] 
sum_ = 0
for i in numbers:
    sum_ += i
    
print(numbers, sum_)


# In[259]:


numbers = [i for i in range(1, 6)] 
sum_ = sum(numbers)
    
print(numbers, sum_)


# In[260]:


numbers = [i for i in range(1, 6)]
# Built-in-function
print(f'Max = {max(numbers)}\nMin = {min(numbers)}\nSum = {sum(numbers)}')


# In[ ]:





# In[98]:


print(numbers)
numbers.index(1)
print(numbers)


# In[261]:


#### List comprehension - shorter way to create arr/dict
# [вираз for значення in колекція]
arr = ['new' for _ in range(10)]
arr


# In[263]:


arr = []
for _ in range(10):
    arr.append('new')
arr


# In[264]:


squares = [i**2 for i in numbers] # List comprehension, and we can use if 
print(squares)


# In[270]:


squares = [i**2 for i in numbers if i % 2 == 0 ] # List comprehension, and we can use if 
print(squares)


# In[274]:


squares = [i**2 if i % 2 == 0 else None for i in numbers ] # List comprehension, and we can use if 
print(squares)


# In[279]:


squares = [str(i**5) for i in numbers]
print(squares)


# In[281]:


# Task about rating
rating = '54, 36, 54'
number_rating = [float(i.strip()) + 1 for i in ratings.split(',')]
print(number_rating)


# In[283]:


str_numbers = ("1.5", "2.3", "5.25")
print(f'String numbers: {str_numbers}')
float_numbers = sum([float(value) for value in str_numbers])
print(float_numbers)
#print(f'Float numbers: {float_numbers}')
#print(f'Float numbers sum: {sum(float_numbers)}')


# In[ ]:





# ## Practice block 1
# 
# 1. Write a Python program to compute the difference between two lists.
# 
#     Sample data: ['a', 'b', 'c', 'd'], ['c', 'd', 'e']
# 
#     Expected Output:
# 
#     first-second: ['a', 'b']
# 
#     second-first: ['e']
#     ```python
#     def compute_difference(first: list, second: list) -> tuple:
#         # write your code here
#         pass
# 
#     def test_compute_difference():
#         result1 = compute_difference(['a', 'b', 'c', 'd'], ['c', 'd', 'e'])
#         assert result1 == (['a', 'b'], ['e'])
# 
#         result2 = compute_difference([], ['c', 'd', 'e'])
#         assert result2 == ([], ['c', 'd', 'e'])
# 
#         result3 = compute_difference([1, 2, 3], [4, 5, 6])
#         assert result3 == ([1, 2, 3], [4, 5, 6])
# 
#         result3 = compute_difference([1, 2, 3], [2, 3, 4])
#         assert result3 == ([1], [4])
#     ```
# 
# 
# 
# 9. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# 
#     You may assume that each input would have exactly one solution, and you may not use the same element twice.
# 
#     You can return the answer in any order.
# ß
#     **Example 1:**
# 
#     Input: nums = [2,7,11,15], target = 9
# 
#     Output: [0,1]
# 
#     Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# 
#     **Example 2:**
# 
#     Input: nums = [3,2,4], target = 6
# 
#     Output: [1,2]
# 
#     **Example 3:**
# 
#     Input: nums = [3,3], target = 6
# 
#     Output: [0,1]
# 
#     ```python
#     def sum_of_two(nums: list, target: int) -> list:
#         # write your code here
#         pass
# 
#     def test_sum_of_two():
#         result1 = sum_of_two([2,7,11,15], 9)
#         assert result1 == [0, 1]
# 
#         result2 = sum_of_two([3,2,4], 6)
#         assert result2 == [1, 2]
# 
#         result3 = sum_of_two([3,3], 6)
#         assert result3 == [0, 1]
#     ```
# 
# 9. Optional (hard): Longest Increasing Sequence
# 
#     Have the function longest_increasing_sequence take the list of positive integers and return the length of the longest increasing subsequence (LIS). A LIS is a subset of the original list where the numbers are in sorted order, from lowest to highest, and are in increasing order. The sequence does not need to be contiguous or unique, and there can be several different subsequences. For example: if arr is [4, 3, 5, 1, 6] then a possible LIS is [3, 5, 6], and another is [1, 6]. For this input, your program should return 3 because that is the length of the longest increasing subsequence.
#     ```
#     Examples
# 
#     Input: [9, 9, 4, 2]
# 
#     Output: 1
# 
#     Input: [10, 22, 9, 33, 21, 50, 41, 60, 22, 68, 90]
# 
#     Output: 7
# 
#     
#     ```
#     ```python
#     def longest_increasing_sequence(arr: list) -> int:
#         # write your code here
#         pass
# 
#     def test_sum_of_two():
#         result1 = longest_increasing_sequence([9, 9, 4, 2])
#         assert result1 == 1
# 
#         result2 = longest_increasing_sequence([10, 22, 9, 33, 21, 50, 41, 60, 22, 68, 90])
#         assert result2 == 7
# 
#         result3 = longest_increasing_sequence([4, 3, 5, 1, 6])
#         assert result3 == 3
#     ```

# In[ ]:





# ### Nesting, copying, and sorting

# In[284]:


nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f'len(two_by_two): {len(nested_list)}')


# In[286]:


nested_list[2][1]


# In[287]:


for i in nested_list:
    for j in i:
        print(j)
    print('\nNext arr\n')


# In[288]:


first_list = [1, 2, 3]
second_list = first_list
second_list[0] = 0
print(first_list) # Який буде результат?


# In[289]:


first_list = [1, 2, 3]
second_list = first_list[:] # [1, 2, 3] [i for i in first_list]
second_list[0] = 0
print(first_list, second_list)


# In[296]:


def some_function(value, temP_list = 'abc'):

    temP_list += value
    print(temP_list)


# In[291]:


def some_function(value, temP_list = []): 

    temP_list.append(value)
    print(temP_list)


# In[308]:


some_function(3) # Що поверне?


# In[303]:


def some_function(value, temP_list = None):
    if temP_list is None:
        temP_list = []

    temP_list.append(value)
    print(temP_list)


# In[301]:


some_function('3')


# In[309]:


some_function.__defaults__ # Звернутись до дефолт значень


# In[311]:


some_function(5)


# In[337]:


unsorted_list = [3, 2, 1, 7, 4]
unsorted_list.sort()
print(f'use sort: {unsorted_list}')


# In[ ]:





# In[319]:


numbers = ['twenty', 'one']
numbers.sort(key = len)
print(numbers)


# In[332]:


numbers = ['2', '1','35', '11']
numbers.sort(key = max)
print(numbers)


# In[ ]:





# In[ ]:





# ## Practice block 2
# 
# 
# 1. Create a list with next values [1, 4, 2, 5]. Create a sorted copy of that list w/o changing the original list.
# 2. Sort the following list by population. Calculate average and total population for cities from this list:
# ```
# [
#     ('New York City', 8550405),
#     ('Los Angeles', 3792621),
#     ('Chicago', 2695598),
#     ('Houston', 2100263),
#     ('Philadelphia', 1526006),
#     ('Phoenix', 1445632),
#     ('San Antonio', 1327407),
#     ('San Diego', 1307402),
#     ('Dallas', 1197816),
#     ('San Jose', 945942),
# ]
# ```
# 
# 

# In[ ]:





# In[ ]:




