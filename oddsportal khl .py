
# coding: utf-8

# In[2]:


import urllib
from selenium import webdriver
import urllib.request
import time
import re
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="/Users/kuoenjui/Desktop/test/chromedriver") # choose the  webdriver location (chrome)
driver.get("https://www.oddsportal.com/hockey/russia/khl/")  # comics url

## change odds viewer
driver.find_element_by_xpath('//*[@id="user-header-oddsformat-expander"]/span').click()
driver.find_element_by_xpath('//*[@id="user-header-oddsformat"]/li[1]/a/span').click()

## click the first one



def fi(a):
    try:
        driver.find_element_by_xpath(a).text
    except:
        return False
def ffi(a):
    if(fi(a)!=False):
         return driver.find_element_by_xpath(a).text



a= dict();
def ell(i,j):
    return ffi('//*[@id="odds-data-table"]/div[1]/table/tbody/tr['+str(i)+']/td['+str(j)+']')


def f(i):
    try:
        a[ell(i,1)]=[ell(i,2), ell(i,3), ell(i,4)]
    except:
        print('')

   

    
    
time.sleep(2)
driver.find_element_by_xpath('//*[@id="tournamentTable"]/tbody/tr[4]/td[2]/a').click()
         
    

    







print(driver.find_element_by_xpath('//*[@id="col-content"]/h1').text)


time.sleep(1)

a= dict();
for i in range(0,10):
        f(i)

        
        
a


## again


# In[3]:


for i in range(0,4):
    time.sleep(5)
    a= dict();
    for i in range(0,10):
        f(i)
    print(a)


# In[ ]:


driver.find_element_by_xpath('//*[@id="tournamentTable"]/tbody/tr[4]/td[2]/a')./click()


# In[ ]:


=

