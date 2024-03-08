#!/usr/bin/env python
# coding: utf-8

# In[10]:


name =input("enter a name")
names=["ahmed","retaj","samah"]
found =False

for i in names:
    if i==name:
        
        found=True
        print("found")
        break
if found==False:
    
    print ("not found")


# In[15]:


#do while loop simulation

while True:
    print("el salamo 3likom")
    userInput=input("if you want to exit type yes/n")
    if userInput.lower()=="yes":
        print("you're out")
        break
        
    
    


# In[12]:


#default parameter putting values if the user didn't enter new ones

def sum(x=5,y=7):
    return x+y
sum(9,8)


# In[ ]:




