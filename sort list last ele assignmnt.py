#!/usr/bin/env python
# coding: utf-8

# In[4]:


list=[(2,5),(1,2),(4,4),(2,3),(2,1)]
def last_ele(n): 
    return n[-1]
def sort_list(tuples):
  return sorted(tuples, key=last_ele)
print(sort_list(list))


# In[ ]:




