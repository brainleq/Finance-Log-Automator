#!/usr/bin/env python
# coding: utf-8

# In[9]:


from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import time

# urls of interest
POST_LOGIN_URL = 'https://venmo.com/groups/sign-in'
REQUEST_URL = 'https://venmo.com/TXOmegas'

# chromedriver initialization
chromedriver_path = "D:\Brian\Documents\chromedriver"
driver = webdriver.Chrome(chromedriver_path)

# initial login post and credentials
driver.get(POST_LOGIN_URL)
username = driver.find_element_by_name("username")
password = driver.find_element_by_name("password")
username.send_keys("") # username here
password.send_keys("") # password here
driver.find_element_by_css_selector(".button").click()

# 60 seconds for 2FA, signal on homepage arrival
home_page = "https://venmo.com/"
success = False
try:
    element = WebDriverWait(driver, 60).until(EC.url_to_be(home_page))
    print("homepage arrived")
    driver.get(REQUEST_URL)
    if driver.current_url == REQUEST_URL:
        success = True
except:
    print("homepage error")
    driver.quit()


# In[10]:


def print_trans_list(trans_list):
    for j in range (len(trans_list)):
        print(str(j) + ": " + trans_list[j].text)


# In[11]:


if success:
    feed_xpath = "/html/body/div[2]/div[8]/div[1]/div[4]/div[2]"
    trans_list = []
    # allow elements to load
    time.sleep(2)
    for i in range (2, 17):
        trans_xpath = "/div[" + str(i) + "]"
        trans_list.append(driver.find_element_by_xpath(feed_xpath + trans_xpath))
    


# In[12]:


account_name = "UT Omega Phi Gamma"
name_list = []
desc_list = []
dollar_list = []
for i in range (len(trans_list)):
    tokenize = trans_list[i].text.split("\n")
    token = " charged "
    # get the person's name
    if "paid" in tokenize[0]:
        token = " paid "
    personel = tokenize[0].split(token, 1)
    name = personel[0]
    if name == account_name:
        name = personel[1]
    # get the description
    desc = tokenize[1]
    # get the dollar amount
    dollar = tokenize[-1]
    dollar_int = ""
    if "+" in tokenize[3]:
        dollar_int = dollar[2:len(dollar)]
    else:
        dollar_int = dollar.replace("$", "")
    name_list.append(name)
    desc_list.append(desc)
    dollar_list.append(dollar_int)
print(name_list)
print(desc_list)
print(dollar_list)

