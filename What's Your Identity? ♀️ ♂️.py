# # What's Your Identity? ♀️ ♂️ (Exercise B)

# This pronoun_ID() function returns the correct pronoun preferences associated with a corresponding gender identity. 

# In[6]:


def pronoun_ID(gender):
    pronouns = '?'
    if gender == 'female':
        pronouns = 'she/her/hers'
    if gender == 'male':
        pronouns = 'he/him/his'
    if gender == 'non-binary':
        pronouns = 'they/them/theirs'
    return pronouns


# In[7]:


pronoun_ID('female')


# In[8]:


pronoun_ID('male')


# In[9]:


pronoun_ID('non-binary')


# In[10]:


pronoun_ID('?')
