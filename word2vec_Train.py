#!/usr/bin/env python
# coding: utf-8

# INFO
# -------------------------------------------------------------
# This script uses NLTK and pyhton re to tokenize corpus and gensim lybrary to train corpus with Word2Vec altgorithm.
# you can change hyperparameters for Word2Vec training depending on your choice.
# 
# ------------------------------------------------------------
# After training process obtained vectors can be uploaded
# 
# -----------------------------------------------------------

# In[1]:


import re
import nltk
import gc


file = open(_your_corpus_,'r',encoding="utf-8")


# In[2]:


gc.collect()


# In[11]:


corpus = file.read()
file.close()


# In[13]:


# Tokenization 
WORD = re.compile(r'\w+')
all_words = []

for sent in nltk.sent_tokenize(corpus):
    all_words.append(WORD.findall(sent))


# In[27]:


# Training

from gensim.models import Word2Vec
word2vec = Word2Vec(all_words, min_count=12,size =300, window = 6, negative = 6 )


# In[28]:


#After training it is a good idea to erase corpus and tokens to free up memory
corpus = None
all_words = None 


# In[29]:


# some predictions on model

word2vec.wv.most_similar(positive = ["sükut"] )


# In[28]:


model = word2vec.wv


# In[30]:


# Saving vectors to txt file vectors can be later used for testing or for feature extraction for NLP tasks. 
# However It is not possible to use this file for more training, for such purposes you shoul store model itself.

model.save_word2vec_format(_vectors_file_, binary =False)


# In[ ]:




