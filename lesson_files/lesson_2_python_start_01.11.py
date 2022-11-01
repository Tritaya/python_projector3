#!/usr/bin/env python
# coding: utf-8

# ### Lesson 2 - 01.11
# Орієнтовно часу на вебінар: 2-2.30 години 
# 	
# > Materials: 
# >    1. [Syntax](https://www.w3schools.com/python/python_syntax.asp) - from syntax to lists        
# >    2. [Basic tips](https://realpython.com/python-beginner-tips/)
# >    3. [Information about all](https://pynative.com/get-started-with-python/) - from start to control flow
# >    4. [Info about print](https://www.w3schools.com/python/ref_func_print.asp)
# >    5. [Data Types](https://webportal.com.ua/data-type-python/)
# 
# > Topics:
# 		> 1. Commands
# 		> 2. Errors
# 		> 3. Variables
# 		> 4. Types  
# 		> 5. Input
# 		> 6. Numbers
# 		> 7. Operation
# 

# In[103]:


print('Hello World!') # Функція виводу в консоль текстової інформації


# In[221]:


print('Some text', 'try seperator','буде зірочка' ,
      sep = '*', # Вказуємо роздільник між текстом
      end = ';' # Вказуємо кінцевий символ
     )  # \n - перехід на наступну строку


# In[ ]:





# ### Type of Errors
# 1. **Syntax** - have more type of errors inside
# 2. **Logic** - when you code work, but with wrong result

# In[111]:


print("Try print")


# In[114]:


# SyntaxError
print("Try Error")


# In[40]:


#  SyntaxError more example
a c = 6


# In[ ]:


# Logic errors


# In[118]:


age = 18
salary = 150000
print('Age of user: ', age)


# #### Характеристика зміною:
#     1. Область допустимих значень
#     2. Діапазон допустимих операцій
#     3. Кількість пам'яті яку займає 

# In[6]:


a = 5 # Assignment operator(Оператор присвоєння)


# In[104]:


type(a) # Повертає тип даних
# int - числовий тип даних( без остачі)
# допустимі операції - всі базові арифметичні(окрім винятків)
# діапозон допустимих значен: inf


# In[106]:


import sys # Імпорт бібліотеки для роботи зі системними значеннями


# In[107]:


print(sys.int_info, # Отримати інформацію для тип даних 
     sep = '\n\n')


# In[142]:


a = 18.11
print(a + 2)


# In[110]:


try_error = 10 + int('5') # unsupported operand 
print(try_error)


# In[130]:


try_float_var = 3.14
a = 10
print(try_float_var + 2)


# In[132]:


print(type(try_float_var), type(1))


# In[60]:


print(try_float_var + a) # Float - має більшу пріоритетність, тому замінуює результат на float


# In[157]:


a, b, c = 16, 5, 6 # Створюємо три змінних
c = float(c)
print(b, a, c, 5 + 1)


# In[158]:


plus = a + b  # Plus value
diff = a - b # Minus value
mult = a * b # Multi value
power_value = a ** 2 # Power з  право наліво читається 

print('Plus  a + b = ', plus)
print('Minus a - b = ', diff)
print('Multi a * b = ', mult)
print('Power a ^ 2 = ', power_value )
print(a / b , a // b, a ** 0.5)


# In[ ]:





# 

# In[161]:


b = 16
print(b)


# In[82]:


# Module, input, practise task, prioriti of operation


# In[162]:


b = b - 2
print(b)


# #### Скорочений запис

# In[ ]:


b += 2 # b = b + 2 
b -= 2 # b = b - 2
b *= 2 # b = b * 2
b /= 2 # b = b / 2


# In[81]:


b **= 2
print(b)


# In[ ]:





# In[ ]:





# In[ ]:





# In[54]:


print(int(bool_var), int(bool_false_var)) # Приймає значення 0  або 1 


# In[210]:


print(123450445)
print(123_450_445) # Можливість зручно записувати великі цифри


# In[215]:


big_int = 123_450_445_0543
print(big_int)


# In[ ]:





# In[ ]:


# Convert type - name_of_type(value_to_convert)


# In[ ]:


print(float(1), 
      int(3.14), 
     )


# In[ ]:


print(
    float('3.14'), type(float('3.14')), '\n',
    int('4'), type(int('4'))
)


# ### Variable name 
# 1. [Main rules](https://www.w3schools.com/python/gloss_python_variable_names.asp) - Use python_style
# 
# > **Python_style** - when we create a var with "_"  
# 
# > **CamelStyle** - when we create a var with other name and start new word in UpperCase

# In[164]:


name_of_user = 'Oleksandr'


# In[26]:


#Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


# In[ ]:


#Illegal variable names:
2myvar = "John"
my-var = "John"
my var = "John"


# In[ ]:





# ### Comments 
# 1. One line start with # 
# 2. More than one line start with ''' and end with '''

# In[167]:


# One line comment, ignore by ide
print('Some text')


# In[173]:


'''
For big text, or try to explain
For big text, or try to explain
For big text, or try to explainFor big text, or try to explain
For big text, or try to explain
For big text, or try to explain
''' 
print('Some text')


# In[179]:


help_value = 10
print(help_value)


# In[180]:


res = help_value - a # Use comments to save info about code
print(res)


# In[ ]:





# ### Input - function for save infromation from user 
# input(text optional)
# 

# In[181]:


input()


# In[184]:


name = input('Enter you name: ')


# In[197]:


print(int(18.1), int(float('18.1')))


# In[198]:


age = int(input('Enter you age: '))


# In[190]:


print(age + 10)


# In[94]:


print(name + name)


# In[ ]:


age_of_user = int(input('Enter you age: '))


# In[ ]:


print(age_of_user, type(age_of_user))


# In[199]:


a = int('a')


# In[202]:


a = int('😂')
print(a)


# In[206]:


smile = '🐅 + 2'
print(smile)


# In[ ]:




