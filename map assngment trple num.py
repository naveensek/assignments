#!/usr/bin/env python
# coding: utf-8

# In[3]:


list1 = [1, 2, 3, 4, 5, 6, 7] 
print('the actual list is:',list1)
list2 = map(lambda x: x + x + x, list1) 
print("the new list with tripled numbers is:",list(list2))


# In[ ]:




