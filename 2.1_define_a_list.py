#!/usr/bin/env python
# coding: utf-8

# In[13]:


# The target list to create from given lists in all tasks below: 
# z = [['x1', 'y1'], ['x2', 'y2'], ['x3', 'y3'], ['x4', 'y4'] , ['x5', 'y5']]

# Task 1
m = ['x1', 'x2', 'x3', 'x4', 'x5']
n = ['y1', 'y2', 'y3', 'y4', 'y5']

new_mn = [ [m[0],n[0]], [m[1],n[1]], [m[2],n[2]], [m[3],n[3]],  [m[4],n[4]] ]
print(new_mn)

# Task 2
k = [['y1', 'x1'], ['y2', 'x2'], ['y3', 'x3'], ['y4', 'x4'] , ['y5', 'x5']]

new_k = [ [ k[0][1], k[0][0] ], 
         [ k[1][1], k[1][0] ], 
         [ k[2][1], k[2][0] ],
         [ k[3][1],k[3][0] ], 
         [ k[4][1], k[4][0] ] ]
print(new_k)

# Task 3
l = ['x1', 'y1', 'x2', 'y2', 'x3', 'y3', 'x4', 'y4', 'x5', 'y5']

new_l = [['x1','y1'], ['x2','y2'], ['x3','y3'], ['x4','y4'], ['x5','y5']]
print(new_l)

# Task 4
o = [['x4', 'y4'], ['x2', 'y2']]
p = [['x1', 'y1'], ['x3', 'y3'], ['x5', 'y5']]

new_op = []
new_op.append(p[0]); new_op.append(o[1]); new_op.append(p[1]); new_op.append(o[0]); new_op.append(p[2])
print(new_op)


# In[ ]:




