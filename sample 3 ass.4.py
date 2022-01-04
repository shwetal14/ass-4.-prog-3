#!/usr/bin/env python
# coding: utf-8

# In[1]:


def square_num(n):
  return n * n
nums = [4, 5, 2, 9]
print("Sample List: ",nums)
result = map(square_num, nums)
print("Square the elements of list:")
print(list(result))


# In[ ]:




