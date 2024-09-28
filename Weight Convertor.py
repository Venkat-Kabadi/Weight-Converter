#!/usr/bin/env python
# coding: utf-8

# In[4]:


weight=float(input("Enter your weight: "))
unit=input("Kilograms or Pounds (K or L): ")

if unit=="K":
    weight=weight*2.205
    unit="Lbs."
    print(f"Your weight is: {round(weight,2)} {unit}")
    
elif unit=="L":
    weight=weight/2.205
    unit="Kilograms."
    print(f"Your weight is: {round(weight,2)} {unit}")
else:
    print(f"{unit} is not valid")


# In[ ]:




