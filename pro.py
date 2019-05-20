#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:


def reverse_word(word):
  return word[::-1]


# In[5]:


reverse_word('junyiacademy')


# In[ ]:


def reverse_word_sen(s):
  w = s.split(" ")
  rw = [reverse_word (i) for i in w]
  rws = " ".join(rw)
  return rws


# In[9]:


s = input("ENTER A SENTENCE:")
print(reverse_word_sen(s))


# In[19]:


count=0
maxint = int(input('Enter an integer: '))
for x in range(1,maxint+1):
  if x%3 == 0 and x%5!=0:
    continue
  if x%5 == 0 and x%3!=0:
    continue
  if x%3 == 0 and x%5 == 0:
    print(x)
    count = count + 1
  else:
    print(x)
    count = count + 1
print("output:" + str(count))


# In[ ]:




