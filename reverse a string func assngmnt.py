#!/usr/bin/env python
# coding: utf-8

# In[3]:


str = "1234abcd"
def reverse(str):
    string = ""
    for i in str:
        string = i + string
    return string
print("The original string is:",str)
print("The reversed string is:", reverse(str))


# In[ ]:





# In[ ]:




