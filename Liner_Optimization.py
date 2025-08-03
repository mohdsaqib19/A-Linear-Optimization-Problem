#!/usr/bin/env python
# coding: utf-8

# ## Problem Statement 
# A company makes three models of desks, an executive model, an office model and a student model. Each desk spends time in the cabinet shop, the finishing shop and the crating shop as shown in the table:

# ### The Give data is

# In[22]:


desk_data = [
    {
        "Type": "Executive",
        "Cabinet_hrs": 2,
        "Finishing_hrs": 2,
        "Crating_hrs": 1,
        "Profit": 1600
    },
    {
        "Type": "Office",
        "Cabinet_hrs": 1.5,
        "Finishing_hrs": 1,
        "Crating_hrs": 2,
        "Profit": 1300
    },
    {
        "Type": "Student",
        "Cabinet_hrs": 1,
        "Finishing_hrs": 1.5,
        "Crating_hrs": 0.5,
        "Profit": 600
    }
]

# Available hours
available_hours = {
    "Cabinet_hrs": 20,
    "Finishing_hrs": 24,
    "Crating_hrs": 20
}


# In[27]:


get_ipython().system('pip install PuLP')


# In[39]:


import pandas as pd
import pulp as p


# In[65]:


data = pd.DataFrame(desk_data)
data


# In[66]:


Lp_prob = p.LpProblem('Problem1', p.LpMaximize)


# In[67]:


Lp_prob


# In[ ]:





# # Decision Variable

# In[68]:


x1 = LpVariable(name="x1", lowBound=0)
x2 = LpVariable(name="x2", lowBound=0)
x3 = LpVariable(name="x3", lowBound=0)


# # Objective function

# In[69]:


Lp_prob += 1600*x1 + 1300*x2 + 600*x3


# # Constraints

# In[70]:


Lp_prob += 2*x1 + 1.5*x2 + 1*x3 <= 20
Lp_prob += 2*x1 + 1*x2+ 1.5*x3 <= 24
Lp_prob += 1*x1 + 2*x2+ 0.5*x3 <= 20


# In[71]:


print(Lp_prob)


# # Solving the LPP

# In[73]:


status = Lp_prob.solve()
print(p.LpStatus[status])


# # Solution

# In[76]:


p.value(x1)


# In[77]:


p.value(x2)


# In[78]:


p.value(3)


# In[80]:


print("x1=",p.value(x1))
print("x2=",p.value(x2))
print("x3=",p.value(x3))


# In[81]:


print("objective = ", p.value(Lp_prob.objective))


# In[ ]:




