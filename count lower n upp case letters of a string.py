#!/usr/bin/env python
# coding: utf-8

# In[4]:


string=('The quick Brow Fox')
count_low=0
count_up=0
for i in string:
      if(i.islower()):
            count_low=count_low+1
      elif(i.isupper()):
            count_up=count_up+1
print("The number of lowercase characters is:")
print(count_low)
print("The number of uppercase characters is:")
print(count_up)


# In[ ]:




