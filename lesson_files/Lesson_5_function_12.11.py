#!/usr/bin/env python
# coding: utf-8

# ### Python lesson 5.  
# #### Create and work with **Function**. Date: 12.11
# > **Main topic**:
# >    1. Test
# >    2. **Function**
#     
# > **Materials**:
# >    1. [Function](https://python-course.eu/python-tutorial/functions.php)
# >    2. [Range function](https://realpython.com/python-range/)
# >    3. [Simple function](https://www.w3schools.com/python/python_functions.asp)
# >    4. [Lambda function](https://www.w3schools.com/python/python_lambda.asp)
#         

# 

# In[237]:


# While - loop
# Task 1. Знайти помилку. Описати що робить код, бажано построчно 
pointer = 0
counter = int(input('Enter number')) # Синтаксчна помилка
while pointer <= counter: # Цикли
    # Тіло циклу
    print(f'Step {pointer} to {counter}')
    pointer +=1 # Синтаксична і логічна помилка


# In[ ]:





# In[ ]:


# Task 2. Знайти суму чисел від 0 до 100
# Створювати змінні, 0
# оператори циклів
# if - stat 
# print 
# range 


# In[ ]:


# Студент 
i = 99
s = i * (i + 1) // 2


# In[241]:


# Студент 
sum_ = 0
for i in range(100):
    sum_ += i # sum_ = sum_ + i
print(sum)


# In[245]:


string = 'string'
print(string[0], string[0:2], string[0::2], string[-1])


# In[ ]:


# Task 3. Розвернути строку 
1. за допомогою цикла 
2. Функцією або slice . Example: 123 -> 321 


# In[249]:


user_string = input('Enter you string: ')
print(f'{user_string} reverse {user_string[::-1]} ')


# In[ ]:





# In[242]:


# Test task 
Create the dictionary with numbers (counts) of vowels in the given string in one line. We consider a, e, i, o, u as vowels (not y).
Example of input: 'Education'
Example of output: count of  vowels: 5 * Потрібно порахувати vowels і вивезти їх кількість 


# In[258]:


# Task 4. Порахувати сумму чисел, введену user. Example: 123 -> 6
string_user = input('Enter number: ')
summ_of_string = 0
counter = 0
for i in string_user:
    print(f'Step {counter} Summ {summ_of_string}')
    counter += 1
    summ_of_string += int(i)
print(summ_of_string)


# In[ ]:





# ### Функція - іменована/анонімна область пам'яті. В середині якої зберігається код.
# (Тип даних функцій - функція, об'єкт в Python)
# >Основні задачі які вирішують функція:
# > 1. Повторне використання коду
# > 2. Розділення програми на логічні блоки
# 
# Для створення функції з іменем використовуємо ключове слово **def** 
# 
# 
# def імя_функції(параметри) -> повертаємий тип (очікуваний): \
#     Тіло функції, в середині цього тіла створюється локальна область видимості

# ### Типи функцій:
# > 1. Функція без параметрів
# > 2. Функція з параметрами
# > 3. Функція з необ параметрами(*args, \***kwargs). 

# In[261]:


pri = print


# In[260]:


pri('Hello World!')


# In[181]:





# In[182]:





# In[267]:


def first_function(): # Створюємо функцію без параметрів, signature 
    # Тіло функції - body
    print('Hello my first function') 


# In[268]:


print(first_function(), first_function(), first_function(), first_function())


# In[270]:


for i in range(1000):
    first_function()


# In[272]:


a = first_function() # Для виклика функції звертаємось до іменні
print(a, type(a)) # Функція завжди повертає результат, якщо функція явно нічого не повертає по замовчуванню буде None


# In[142]:


print(type(a), a, first_function())


# In[139]:


first_function()


# In[138]:





# In[155]:


def add(a, b) -> int: # Створити функцію з двома параметрами, порядок передачі аргументів важливий!
    print(f'A = {a} B = {b}')
    return a + b


# In[274]:


result = add(5, 7)
print(result, type(result))


# In[156]:


print(add(5, 7))


# In[275]:


print(add(b = 8, a = 5))


# In[277]:


print(add(b = '8', a = '5'))


# In[278]:


a, b = 15, True


# In[279]:


def minus(a, b):
    print(f'A = {a} B = {b}')
    return a - b


# In[284]:


print(minus(16.0, 18))


# In[285]:


def sum_of_two_numbers(a, b):  # signature
    # body
    sum_result = a + b
    return sum_result
    # print(f'Result is {sum_result}')


result = sum_of_two_numbers(1, 2)
print(result)
print(sum_of_two_numbers(30, 50))
print('a=', 1, 'b=', 2, 'sum_of_two_numbers(1,2)', sum_of_two_numbers(1,2))


# In[286]:


def get_int_from_input():  # signature
    # body
    input_value = input('input something')
    return int(input_value)
    print(f'Result is {sum_result}')


result = get_int_from_input()
print(result, '*')


# In[287]:


def all_math(a, b, operation):
    match operation:
        case '+':
            return a + b
        case '-':
            return a - b
        case '*':
            return a * b
        case '/':
            return a / b
        case _ :
            return None


# In[290]:


print(all_math(5, 10, '-'), all_math(5, 10, '+'))


# In[190]:


# Task 5. Створити функцію, і вивезти сумму чисел від 0 до числа який введе користувач.


# In[295]:


# Функціонал: def, return, for/while, range, input, print
# Крок 1 - створити функцію, 1 - змінну(signa) 
# Крок 2 - створити змінну для save result
# Крок 3 - створити цикл буде проходити в range
# Крок 4 - повернути результат 


# In[303]:


def sum_of_number(user_number):
    sum_of_number = 0
    for i in range(user_number):
        sum_of_number += i
    return (sum_of_number)

user_number = int(input('Enter number: '))
    
print(sum_of_number(user_number))


# In[192]:


# Task 6. Створити функцію, яке повертає сумму чисел від 0 до числа який введе користувач, числа повинні бути even


# In[300]:


def sum_even_range(up_lim):
    # (up_lim // 2) кількість парних чисел
    # up_lim - up_lim % 2 останнє парне число
    # 2 перше парне число, якщо не рахувати 0
    return (up_lim // 2) * (2 + up_lim - up_lim % 2) // 2


# In[ ]:





# ### Practice section 1:
# 
# 1. Write a program that caluculate Fibonacci series. The Fibonacci series is a series of numbers in which each number is the sum of the two preceding numbers. The first two numbers are 1 and 1. The third number is 1 + 1 = 2, the fourth number is 1 + 2 = 3, and so on. Number of iterations should be taken from user input.
# 

# In[305]:


# Опціальні параметри 
def try_option(result = 'Hello'):
    print(f'Result: {result}')


# In[304]:


print(try_option(), try_option('My hello'))


# In[208]:


def try_option_with_name(surname, name = 'User'):
    print(f'Hello {name} {surname}')


# In[306]:


try_option_with_name()


# In[307]:


try_option_with_name('Ukr')


# #### Порядок аргументів строгий, спочатку йде обов'язкові аргументи, потім опціональні 

# ### Practice section 2
# 
# 1. Write a program that iterated from 0 to 100 and prints out the number if it is divisible by 3.
# 2. Get a number from user input and iterate from 0 to that number. 
#     
#     1. Print 'foo' if the number is divisible by 3. 
#     2. Print 'bar' if the number is divisible by 5. 
#     3. Print 'foobar' if the number is divisible by both 3 and 5.
# 

# In[212]:


def multiply_two_numbers(
    zero_argument,
    first_argument = '2',
    second_argument = '3'
):  # signature
    # body
    sum_result = zero_argument + first_argument +  second_argument
        
    return sum_result


# In[309]:


result = multiply_two_numbers('1', '4', '5')
print(result)


# In[312]:


result = multiply_two_numbers('1', second_argument='4')
print(result)


# In[ ]:





# In[216]:


# types
# Для того щоб вказати тип через : вказуємо тип, для того щоб вказати очікуваний тип -> після цього вказуємо тип
def sum_values(first_value: int, second_value: int) -> int:
    return first_value + second_value


# In[313]:


print(sum_values('4', '5'), sum_values(5,10))


# In[318]:


def read(a: bool = 'Hello'):
    print(a)


# In[317]:


read('Text')


# ## Practice block 3: 
# 
# 1. Write a function called square() with one argument of int type and returns the value of that number raised to the second power.
# 2. Write a program called convert_cel_to_fahr() that takes a temperature in Celsius and returns the equivalent temperature in Fahrenheit. It should take a number as an argument from user input and return a number to the console. 
# 3. Write a function that implement case swapping. It should return the same result as swapcase() method. Your function should accept one str argument and convert all lower case values to upper case and vice versa. 
# ```python
# def swapcase(input_string: str) -> str:
#     # do something
# 
# print(swapcase('HelLo')) 
# 
# > 'hELlO
# ```

# #### Args - створюємо нескінчену кількість значень, для використання використовуємо \*

# In[322]:


# *args
def function_with_args(*args):
    sum(args)
    print(f'args: {sum(args)}')


# In[324]:


function_with_args(1, 2, 3, 4, 5, 6)


# In[339]:


def ar(param1, *args):
    param1 += 1
    return 
    
test_args = ar(1, 2,3,4,5)


# In[340]:


# + , + 
print('1' + '2', 1 + 2)


# In[332]:


# *args
def function_with_args1(param1, param2, param3 ,*args):
    print(f'Param1 = {param1}')
    print(f'Param2 = {param2}')
    print(f'Param3 = {param3}')
    print(f'Param args = {args}')
    
    sum(args)
    print(f'args: {s}')



# In[331]:


function_with_args1(1, 2, 3, 4, 5, 6)


# In[ ]:


# Hard mode


# **Task 1**. Дискримінант. Створіть функцію з іменем **discriminant**.\
# Функція повинна приймати на вхід a, b, c, choose. Де a, b, c - це аргументи функції, choose - опціональний параметр, вибору способу рішення(дискримінант або Вієта, 1 - disc, 2 - Вієта) \
# Функція повинна повертати в залежності від параметрів один/два кореня або їх відсутність. 
# 
# Example:\
#     **Input**: a = 5, b = -8, c = 3 \
#     **Output**: x = 1, x = 0.6 
# Результати округлювати до 2 знаку. Функція повинна перевіряти тип аргументів(int повинен бути). 

# In[ ]:


# Крок 1: допустимі типи, isinstance, type, [int, float, bool]
# Крок 2: Ділення на 0, etc....
# Крок 3: без бібліотек!!!!
# Крок 4: Оптимальність 
# Крок 5: перевірка назв 
# Крок 6: побітові операції + винагорода 
# Крок 7: Обмеженна 3 ступені
# Крок 8: тільки цикли, функції, строки-числа, built-in-function(sum, len) можна
*На листочку


# In[ ]:





# In[114]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




