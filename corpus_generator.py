#!/usr/bin/env python
# coding: utf-8

# INFO 
# 
# ------------------------------------------------------------------------------
# This is a script for generating corpus from several txt files and filtering
# 
# ----------------------------------------------------------------------
# 
# 
# Note that you might need to change filtering options depending on your data since this script 
# was originally written for data in the Azerbaijani language
# 
# -------------------------------------------------------------------------------------------
# 
# simplest way to change filtering is to switch next regex with characters in your alphabet (and optionally few more puntuations or numbers) 
# in following line. It will erase any other character that is not mentioned in regex.  
# text =re.sub("[^qüertyuiopöğasdfghjklıəzxcvbnmçşi. \.]","",text)
# 
# ----------------------------------------------------------------------------------------
# 

# In[1]:


import re, string, os
files = []


# In[3]:


# every txt file within directory one by one, filters them and appends them to the <files> list

for file in os.listdir(_directory_name_):
    if file.endswith('.txt'):
        text = (open("raw/" + i, encoding ="utf-8")).read()
        text = text.replace(u'\xa0', u'').replace(u'\n', u' ').replace("Ģ","ş").replace("Ġ","i").replace(","," ").replace(":"," ").lower()
        text = text.replace(u'...', u'.').replace(u'...', u'.').replace(u'..', u'.').replace(u".", u" . ")
        text =re.sub("[^qüertyuiopöğasdfghjklıəzxcvbnmçşi. \.]","",text)
        files.append(text)
        


# In[4]:


for i in os.listdir("filter"):
    if i.endswith('.txt'):
        a = (open("filter/" + i, encoding ="utf-8")).read()
        a = a.replace(u'\xa0', u'').replace(u'\n', u'. ').replace("Ģ","ş").replace("Ġ","i").replace(","," ").replace(":"," ").lower()
        a = a.replace(u'...', u'.').replace(u'...', u'.').replace(u'..', u'.').replace(u".", u" . ")
        a =re.sub("[^qüertyuiopöğasdfghjklıəzxcvbnmçşi. \.]","",a)
        files.append(a)


# In[11]:


# sample for filtering one file instead of whole directory
a = (open(_your_file_, encoding ="utf-8")).read()
a = a.replace(u'\xa0', u'').replace(u'\n', u'. ').replace("Ģ","ş").replace("Ġ","i").replace(","," ").replace(":"," ").lower()
a = a.replace(u'...', u'.').replace(u'...', u'.').replace(u'..', u'.').replace(u".", u" . ")
a =re.sub("[^qüertyuiopöğasdfghjklıəzxcvbnmçşi. \.]","",a)
files.append(a)


# In[12]:


#merging all filtered texts into one corpus
corpus = ' '.join(files)


# In[13]:


# creating file to upload corpus 

file = open("corpus.txt","w",encoding = "utf-8")
file.write(corpus)
file.close()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




