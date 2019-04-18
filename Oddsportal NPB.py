
# coding: utf-8

# In[1]:


import urllib
from selenium import webdriver
import urllib.request
import time
import re
from selenium.webdriver.common.keys import Keys
import matplotlib.pyplot as plt
import numpy as np


driver = webdriver.Chrome(executable_path="/Users/kuoenjui/Desktop/test/chromedriver") # choose the  webdriver location (chrome)
driver.get("https://www.oddsportal.com/baseball/japan/npb/")  # comics url

## change odds viewer
def view():
    try:
            driver.find_element_by_xpath('//*[@id="user-header-oddsformat-expander"]/span').click()
            driver.find_element_by_xpath('//*[@id="user-header-oddsformat"]/li[1]/a/span').click()
    except:
            driver.find_element_by_xpath('//*[@id="user-header-oddsformat-expander"]/span').click()
            driver.find_element_by_xpath('//*[@id="user-header-oddsformat"]/li[1]/a/span').click()

view()
view()


## click the first one

def fi(a):
    try:
        driver.find_element_by_xpath(a).text
    except:
        return False
def ffi(a):
    if(fi(a)!=False):
         return driver.find_element_by_xpath(a).text
def ell(i,j):
    return ffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr['+str(i)+']/td['+str(j)+']')
def f(i,x):
    try:
        x[ell(i,1)]=[ell(i,2), ell(i,3), ell(i,4)]
    except:
        print('')


   

    
time.sleep(2)

######### the main code:
         
    
    
def tryc(f):
    try:
        driver.find_element_by_xpath(f).click()
    except:
        print('error')
        

                
def operation(i):
              tryc('//*[@id="tournamentTable"]/tbody/tr['+str(i)+']/td[2]/a')
              print(driver.find_element_by_xpath('//*[@id="col-content"]/h1').text)
              time.sleep(1)
              x= dict();
              for i in range(1,10):
                     f(i,x)
              time.sleep(1)
              driver.back()
              return x
        
        
        
        


# In[3]:



### plotblock
a=operation(4)
plt.style.use('seaborn-whitegrid')
import numpy as np
b=list()
for i in range(0,len(a)):
    b.append(float(a[list(a.keys())[i]][0]))
c=list()
for i in range(0,len(a)):
    c.append(float(a[list(a.keys())[i]][1]))
    x = list(a.keys())
y = b
z=c
plt.figure(figsize=(8,4))
plt.plot(x, y,'o', color='green')
plt.plot(x, z,'o', color='red')
plt.title(driver.find_element_by_xpath('//*[@id="tournamentTable"]/tbody/tr[4]/td[2]/a').text)
plt.xlabel('Company')
plt.ylabel('odds')




a=operation(5)
plt.style.use('seaborn-whitegrid')
import numpy as np
b=list()
for i in range(0,len(a)):
    b.append(float(a[list(a.keys())[i]][0]))
c=list()
for i in range(0,len(a)):
    c.append(float(a[list(a.keys())[i]][1]))
    x = list(a.keys())
y = b
z=c
plt.figure(figsize=(8,4))
plt.plot(x, y,'o', color='green')
plt.plot(x, z,'o', color='red')
plt.title(driver.find_element_by_xpath('//*[@id="tournamentTable"]/tbody/tr[5]/td[2]/a').text)
plt.xlabel('Company')
plt.ylabel('odds')




a=operation(6)
plt.style.use('seaborn-whitegrid')
import numpy as np
b=list()
for i in range(0,len(a)):
    b.append(float(a[list(a.keys())[i]][0]))
c=list()
for i in range(0,len(a)):
    c.append(float(a[list(a.keys())[i]][1]))
    x = list(a.keys())
y = b
z=c
plt.figure(figsize=(8,4))
plt.plot(x, y,'o', color='green')
plt.plot(x, z,'o', color='red')
plt.title(driver.find_element_by_xpath('//*[@id="tournamentTable"]/tbody/tr[6]/td[2]/a').text)
plt.xlabel('Company')
plt.ylabel('odds')



a=operation(7)
plt.style.use('seaborn-whitegrid')
import numpy as np
b=list()
for i in range(0,len(a)):
    b.append(float(a[list(a.keys())[i]][0]))
c=list()
for i in range(0,len(a)):
    c.append(float(a[list(a.keys())[i]][1]))
    x = list(a.keys())
y = b
z=c
plt.figure(figsize=(8,4))
plt.plot(x, y,'o', color='green')
plt.plot(x, z,'o', color='red')
plt.title(driver.find_element_by_xpath('//*[@id="tournamentTable"]/tbody/tr[7]/td[2]/a').text)
plt.xlabel('Company')
plt.ylabel('odds')







### plotblock
a=operation(8)
plt.style.use('seaborn-whitegrid')
import numpy as np
b=list()
for i in range(0,len(a)):
    b.append(float(a[list(a.keys())[i]][0]))
c=list()
for i in range(0,len(a)):
    c.append(float(a[list(a.keys())[i]][1]))
    x = list(a.keys())
y = b
z=c
plt.figure(figsize=(8,4))
plt.plot(x, y,'o', color='green')
plt.plot(x, z,'o', color='red')
plt.title(driver.find_element_by_xpath('//*[@id="tournamentTable"]/tbody/tr[8]/td[2]/a').text)
plt.xlabel('Company')
plt.ylabel('odds')




a=operation(9)
plt.style.use('seaborn-whitegrid')
import numpy as np
b=list()
for i in range(0,len(a)):
    b.append(float(a[list(a.keys())[i]][0]))
c=list()
for i in range(0,len(a)):
    c.append(float(a[list(a.keys())[i]][1]))
    x = list(a.keys())
y = b
z=c
plt.figure(figsize=(8,4))
plt.plot(x, y,'o', color='green')
plt.plot(x, z,'o', color='red')
plt.title(driver.find_element_by_xpath('//*[@id="tournamentTable"]/tbody/tr[9]/td[2]/a').text)
plt.xlabel('Company')
plt.ylabel('odds')







