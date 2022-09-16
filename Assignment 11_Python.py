#!/usr/bin/env python
# coding: utf-8

# In[6]:


spam = 10
assert spam >= 10
print('The spam variable is less than 10.')


# In[15]:


assert(eggs.lower() != bacon.lower()
 print('The eggs and bacon variables are the same!')


# In[16]:


eggs = 'hello'
bacon = 'good bye'


# In[20]:


assert eggs.lower() != bacon.lower(), 'The eggs and bacon variables are the same!' or assert eggs.upper() != bacon.upper(), 'The eggs and bacon variables are the same!'


# In[21]:


assert False, 'This assertion always triggers.'


# In[24]:


import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -%(levelname)s - %(message)s')


# In[25]:


import logging

logging.basicConfig(filename='programLog.txt', level=logging.DEBUG,

format=' %(asctime)s - %(levelname)s - %(message)s')

DEBUG, INFO, WARNING, ERROR, and CRITICAL
# In[26]:


logging.disable(logging.CRITICAL)

You can disable logging messages without removing the logging function calls. You can selectively disable lower-level logging messages. You can create logging messages. Logging messages provides a timestamp.The Step button will move the debugger into a function call. The Over button will quickly execute the function call without stepping into it. The Out button will quickly execute the rest of the code until it steps out of the function it currently is in.
# In[ ]:


After you click Go, the debugger will stop when it has reached the end of the program or a line with a breakpoint.


# In[ ]:


A breakpoint is a setting on a line of code that causes the debugger to pause when the program execution reaches the line.

