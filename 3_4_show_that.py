#!/usr/bin/env python
# coding: utf-8

# In[3]:


counter = 0
for n in range(1,100):
  factorial1 = 1
  for i in range(1, n+1):
    factorial1 = factorial1 * i
  factorial2 = factorial1 * (n+1)
  if ((int((factorial1 + factorial2)**0.5))**2) == (factorial1 + factorial2):
    counter += 1

counter == 1

