#!/usr/bin/env python
# coding: utf-8

# In[4]:


import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')

x = [1, 2, 3, 4]
y = [10, 15, 13, 18]

plt.plot(x, y)
plt.show()


# In[5]:


import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
sales = [100, 120, 150, 130, 170]

plt.plot(days, sales)
plt.title("Sales Trend")
plt.xlabel("Day")
plt.ylabel("Sales")
plt.show()


# In[8]:


names = ["Aman", "Rahul", "Priya"]
marks = [80, 90, 85]

plt.bar(names, marks)
plt.title("Student Marks")
plt.show()


# In[9]:


plt.barh(names, marks)
plt.show()


# In[10]:


labels = ["A", "B", "C"]
sizes = [40, 35, 25]

plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Share Distribution")
plt.show()


# In[11]:


data = [10, 12, 15, 15, 18, 20, 21, 22, 22, 22, 25]

plt.hist(data, bins=5)
plt.title("Distribution")
plt.show()


# In[12]:


hours = [1, 2, 3, 4, 5]
marks = [35, 45, 60, 70, 85]

plt.scatter(hours, marks)
plt.title("Study Hours vs Marks")
plt.xlabel("Hours")
plt.ylabel("Marks")
plt.show()


# In[14]:


scores = [50, 55, 60, 65, 70, 75, 80, 100]

plt.boxplot(scores)
plt.title("Score Distribution")
plt.show()


# In[15]:


x = [1, 2, 3, 4]
y = [3, 5, 7, 9]

plt.fill_between(x, y)
plt.show()


# In[16]:


plt.step([1, 2, 3], [10, 20, 15])
plt.show()


# In[20]:


x = [1, 2, 3]
y = [15, 20, 15]
error = [1, 2, 3]

plt.errorbar(x, y, yerr=error, fmt="o")
plt.show()


# In[ ]:




