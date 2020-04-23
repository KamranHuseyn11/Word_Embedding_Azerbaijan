#!/usr/bin/env python
# coding: utf-8

# INFO
# 
# --------------------------------------------------------------------------
# 
# This script shows how to use stored vectors after training and some samples for intrinsic testing, word pair and word analogy testing 
# 
# ---------------------------------------------------------------------------
# 
# Note: Keyedvectors module only supports Word2vec format. You have to transform glove vectors to
# Word2Vec format first in order to use them with this model 
# 
# -----------------------------------------------------------------------------------
# 

# In[8]:


from gensim.models import KeyedVectors
from gensim.models import Word2Vec


# In[ ]:





# In[20]:


# for loading word2vec

model = KeyedVectors.load_word2vec_format( _your_vectors_, encoding ="utf-8")


# In[9]:


# for loading glove 

glove2word2vec(_your_glove_vectors_file_, _new_vectors_file_)
model = KeyedVectors.load_word2vec_format(  _new_vectors_file_, encoding ="utf-8")


# ------------------------------------------------------------
# Some testing with model
# 
# -------------------------------------------------------
# 

# In[19]:


# word pairs
print(model.most_similar(positive = ["ev"],topn=3) )


# In[1]:


# Word analogy,   mən for məndə, sən for ?  
print(model.most_similar(positive = ["məndə","sən"], negative = ["mən"],topn=3))


# In[29]:


# finiding most similiar word from a pool of words
model.most_similar_to_given("ana",["ağ","süd","qadın","əli","vəli","baba","və"])


# In[20]:


# word analogy with other method

model.similar_by_vector( model_glove.get_vector("ata")  - model_glove.get_vector("kişi") + model_glove.get_vector("qadın")) 


# In[38]:


# word pairs without probabilities 
for _tuple in model.most_similar("ata"):
    if (_tuple[1] > 0.60):
        print(_tuple[0])


# ------------------------------------------
# 
# Intrinsic Evaluation:
# 
# you can test your model for semantic and syntactic analogies. to do this you need prepare questions.txt file and run it with following code   
# 
# ---------------------------------------
# 
# It is recommended to build semantic and syntactic questions separately.
# for creating questions please refer to sample_questions.txt in the repository.
# 
# -------------------------------------------

# In[ ]:


print (f" syntactic score: - {model.evaluate_word_analogies('questions_sytactic.txt')[0]}")
print (f" semantic score: - {model.evaluate_word_analogies('questions_semantic.txt')[0]}" ) 


# In[ ]:


# for verbose results 

model.evaluate_word_analogies('questions_sytactic.txt')


# In[238]:





# In[ ]:




