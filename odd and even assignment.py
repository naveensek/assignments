#!/usr/bin/env python
# coding: utf-8

# In[10]:


list_of_numbers= [1,2,3,4,5,6,7,8,9]
count_even=0
count_odd=0
for numbers in list_of_numbers:
    if numbers%2==0:
        count_even=count_even+1
    else:
        count_odd=count_odd+1
print("number of even numbers in the list are: ",count_even)
print("number of odd numbers in the list are: ", count_odd)


# In[ ]:




