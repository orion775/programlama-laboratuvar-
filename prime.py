#!/usr/bin/env python
# coding: utf-8

# In[28]:


def asal_carpan(n):
    x = 5
    liste = []
    for i in range(n):
        if(n%2 == 0):
            liste.append(2)
            n = n/2
        elif(n%3 == 0):
            liste.append(3)
            n = n/3
        elif(n%x == 0):
            liste.append(x)
            n = n/x
        else:
            x += 2
            
    return liste
asal_carpan(70)


# In[1]:


liste_2 = [4, -3, 2, -1, -2, 6, -5]
maximum = liste_2[0]
toplam = 0
n = len(liste_2)
for i in range(n):
    for j in range(i+1, n):
        toplam = 0
        
        for k in range (i, j+1):
            toplam += liste_2[k]
            if(toplam > maximum):
                maximum = toplam
                
print(maximum)


# In[ ]:




