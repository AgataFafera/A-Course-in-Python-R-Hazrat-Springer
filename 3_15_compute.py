#!/usr/bin/env python
# coding: utf-8

# In[2]:


my_sum = 0

for i in range(1,2023):
    my_sum += ( ( 1 + ( 1 / i**2 ) ) + ( 1 / ( i+1**2) ) ** 0.5 )
               
print(my_sum)


# In[ ]:




