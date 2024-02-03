#!/usr/bin/env python
# coding: utf-8

# In[22]:


# According to Python, the expression from the task is equal to 3.9999999999999996 so it returns False while compared to 4.
# I decided to use isclose method from math library to solve that.

import math

expression_result = ((64 ** (1/3)) * ((2 ** 2) + (1/2) ** 2) - 1) ** 0.5
expected_result = 4

if math.isclose(expression_result, expected_result):
    print("The expression is approximately equal to 4.")
else:
    print("The expression is not equal to 4.")
    
    
((64 ** (1/3)) * ((2 ** 2) + (1/2) ** 2) - 1) ** 0.5 == 4

