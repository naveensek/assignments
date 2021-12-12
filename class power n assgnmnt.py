#!/usr/bin/env python
# coding: utf-8

# In[2]:


class power_n:
   def power(self, x, n):
        if x==0 or x==1 or n==1:
            return x 

        if x==-1:
            if n%2 ==0:
                return 1
            else:
                return -1
        if n==0:
            return 1
        if n<0:
            return 1/self.power(x,-n)
        val = self.power(x,n//2)
        if n%2 ==0:
            return val*val
        return val*val*x

print(power_n().power(10,2));


# In[ ]:




