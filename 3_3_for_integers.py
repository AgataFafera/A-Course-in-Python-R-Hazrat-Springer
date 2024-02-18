#!/usr/bin/env python
# coding: utf-8

# In[2]:


n_list = []

for n in range(2, 201):
    factorial = 1
    for i in range(1, n):
        factorial = factorial * i
    if (factorial + 1) % n == 0:
        n_list.append(n)

len(n_list) == 46

