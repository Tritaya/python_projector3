#!/usr/bin/env python
# coding: utf-8

# ### Lesson 11. Network: 08.12
# Plan:
# > 1. API
# > 2. Protocol
# > 3. HTTP/URL
# > 4. HTML/JSON
# > 5. Status Code
# 
# 
# Materials: 
# > 1. [URL](https://developer.mozilla.org/ru/docs/Learn/Common_questions/What_is_a_URL)
# > 2. [Коди Валют](https://www.iban.ru/currency-codes)
# > 3. [Weather API](https://openweathermap.org/api)
# > 4. [Rest API for beg](https://mlsdev.com/blog/81-a-beginner-s-tutorial-for-understanding-restful-api)
# > 5. [DNS work](https://howdns.works/ep1/)

# In[ ]:





# # What is API? (Application programming interface)
# 
# ## I - interface
# 
# Interface - thing that allows to control way how something works through options that are exposed to user. Magic under the hood is completely abstracted away from user. 
# 
# ### GUI
# 
# Interfaces might be provided through GUI. GUI (Graphical User Interface) is a graphic way to interact with user. Due to interfaces are abstracted away from user, user don`t need to know how it works internally, he needs only to know how to use it. While GUI was made for end user, API was made for developers.
# 
# Developer that provides you an interface knows how implementation of this interface work. When you use some interface, you need how to use it, but not how it works. Play/Pause button is an interface to play a media file. Also, dev uses Media Player API (OS interface) when implement this button
# 
# As an user of this interface, you don`t need to know how it works, You only need to know what you should use
# 
# UI was created for user who use the interface
# API was created for application programmer
# 
# 
# 

# ## API
# 
# API is a tool for software developer. It provides you an abstraction for different things 
# 
# In a broader sense, API is a set of functions that are exposed to user, as example random module is also an API that provides some methods with proper way how to us it. You don`t need to know how random module works internally, you just need to know how to use it. When you want to make a tea, you don't need to know how kettle works, you just make it through the API.
# 
# All of us has different internet browsers, but they all might open the same webpage. All that is due to same Web API that being used by all of them.
# 
# 
# Python provides you many API. For example, random module. You don't need to know how it works, you can just use it. Same with `print` function etc
# 
# Same things with a file system interface. The same file can work on any OS
# 
# Also, same sites work in different browsers in the same way. It works because all of them are using the same web interface
# 
# By using them, we don`t need to recreate the wheel every time. When you write your own program, you can use already implementing APIs and focus on a Business logic
# 
# 

# ### Remote APIs
# 
# People use remote API because they provide much more space, speed and quality. For example, Shazam. You can't store all songs on your local device. But you can use an API for that. You don't need to know how it works. You can just use it. Same with translation, face/plant recognition etc 

# ## REST (Representational state transfer)
# 
# REST is interface that help to use APIs over the network. It`s one of the possible interfaces, but now it's a standard de-facto (like Xerox or Pampers)
# 
# Now, we use an APIs that work on a REST standard. We call them `RESTfull`

# ## How WEB works?
# 
# ### Client - Server architecture
# 
# Our browsers is a client. I type URL in search field of our browsers. When we type URL it has following structure - 
# 
# > http://google.com
# 
# > HTTP -> is a Hypertext Transfer Protocol
# 
# *Protocol* is a way that define a way how to communicate
# 
# For example 
# > Слава Україні -> Героям слава
# 
# Same thing for HTTP. It has types. Basic type (method) here is `Get`. It means that we want to receive some data. Server generate some staff and return a response
# 
# ![image](https://intellipaat.com/blog/wp-content/uploads/2021/09/image-99.png)
# 
# The most important part of this response is a body. Usually it`s a HTML data or a JSON object
# 
# With this response, browser render a webpage. It might repeat over and over. Whenever you click the button, browser make new request.
# 
# 

# In[ ]:





# **Protocol**: 
# > 1. http:// - protocol (https)
# > 2. ftp:// - file transfer protocol
# > 3. smtp:// - simple mail transfer protocol
# > 4. ws:// (wss) 
# 
# **Domain** (IPv4, IPv6):
# google.com, facebook.com, developer.mozilla.org -> 99.86.4.33 (DNS)
# 
# > Value inside: 0-255.0-255.0-255.0-255 (192.172.0.1)
# 
# 
# 192.172.0 \
# 192.172.0.1.2 \
# 256.192.1.1
# 
# localhost -> 127.0.0.1
# 
# **Port**
# > 1. http - 80
# > 2. https - 443
# > 3. smtp - 22
# 
# 5000+
# 0 - 65535

# In[ ]:





# ### Stateless
# 
# HTTP doesn`t store any state between our requests. It means that protocol is stateless. It means that you should provide state in each request if you need.
# 
# ### Headers
# 
# Both request and response have some important information that stores in headers. It help to communicate between server and client and set some additional information (language, type os the content, status code)
# 
# ### Status code. 
# 
# status code is one of the important headers. You might saw some of them (404). Standard HTTP has some group of status code
# 
# 1xx - informational response 
# 
# 2XX - success 
# 
# 3XX - redirection
# 
# 4XX - client errors
# 
# 5XX -  server errors

# ### Resources
# 
# In word URL, R stands for resources. Resource is a reference to object in our domain. Almost everything is a resource or collection of resources
# 
# ![web](images/web_2.jpg)
# 
# To do something with a resources, we use a CRUD operation which is Create, Read, Update, Delete

# In[ ]:





# #### CRUD
# **C** - Create(створити)  
# **R** - Read/Rewrite(прочитати) \
# **U** - Update(оновити) \
# **D** - Delete(видалити)

# #### Read
# 
# When we retrieve in information, we read it. To do that, we use Get HTTP method. Usually you receive JSON data type as a response
# 
# show example in a browser
# 
# #### Post
# 
# We use post to add some information on a server 
# 
# #### Patch
# 
# We use patch/put to update some information on a server 
# 
# #### Delete
# 
# We use delete to delete some information from a server 

# In[ ]:





# ### Practice
# 
# With this knowledge you can build whatever you want

# In[5]:


import requests # бібліотека для роботи 


# In[64]:


res_monobank = requests.get('https://api.monobank.ua/bank/currency')


# In[65]:


res_monobank.status_code


# In[20]:


res_monobank.json()[:5:]


# In[66]:


for obj in res_monobank.json():
    print(f'Object is {obj}, \nType is{type(obj)}', end = '\n\n')


# In[67]:


my_currencies = {
    980: '🇺🇦',
    840: '🇺🇸',
    978: "🇪🇺",
    # 826: '🇬🇧',
}

my_rates = []
for obj in res_monobank.json():
    #print(obj.keys())
    if obj['currencyCodeA'] in my_currencies and  obj not in my_rates:
        my_rates.append(obj)

print(my_rates)


# In[69]:


for obj in my_rates:
    #print(obj)
    print(f"Країна: {my_currencies[obj['currencyCodeA']]} Купівля {obj['rateBuy']} Продаж: {obj['rateSell']}")


# In[ ]:





# #### Вивезти з API(приватбанка) курс валют для:
# 1. USA
# 2. EURO
# 3. GBR
# 4. PLN
# 5. Свою валюту
# 
# * Написати Test
# * Вивезти курс валюти від користувача
# * Робити перевірки на status code
# * Написати це функцію
# * Залити на git(flake8 use, requirments, config.cfg)

# In[72]:


resp = requests.get('https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=5') # Отримати 


# In[73]:


resp.status_code


# In[75]:


resp.json()


# In[ ]:





# In[76]:


### Spotify Api


# In[59]:


MY_SECRET_TOKEN = 'BQBIxgccIg5E0XsmY1Ia2laCKSiejIGryLbrAqvpAgAeLU1Mv-gwNKohZj0pLezO0Yv0jnRBw3MpdF_b_WCi5QSBy_-bPCoery3vocvmTnA3zbn3CrPhxK5VX-XiF1FpphNf8_U_nbjLprT1mdzFxTGJzjeo73puYeD2bopzBouAWYa5UGStfZ_Hbr2ta5LR6M'


# In[57]:


stotify = requests.get('https://api.spotify.com/v1/search')


# In[58]:


stotify.status_code


# In[60]:


spotify_resp = requests.get(
    'https://api.spotify.com/v1/search',
    headers={
        'Authorization': f"Bearer {MY_SECRET_TOKEN}"
    },
    params={
        'q': 'queen!',
        'type': "track,artist"
    }
)


# In[61]:


for obj in spotify_resp.json():
    print(f'obj: {spotify_resp.json()[obj]}')



# ## Practice
# 
# 1. Create a program that will ask user to search a word. Search this word in Giphy (use their API). Return links to these GIFs as a result
# 2. Взяти API-weather, розпарсити і вивезти погоду від користувача(вводить локацію, по цій локації повернеться погода, вологість і тд) https://openweathermap.org *Потрібна реєстрація і створення свого api-ключа
# 3. Вивезти всіх космонавтів(кількість і імена) http://api.open-notify.org/astros.json
# 
# 
# 

# In[ ]:





# In[ ]:




