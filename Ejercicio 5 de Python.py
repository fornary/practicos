#!/usr/bin/env python
# coding: utf-8

# 
# ### 5) Crear una tupla en Python con el nombre de “Historial” la cual contenga los siguientes valores:
#       2350, 5960, 23000, 1000, 8900
# Que representa montos de atención en pesos por diferentes servicios/consultas de la mascota “Puppy”. Calcular el monto total gastado a lo largo del tiempo por atención de “Puppy”. Si el gasto efectuado es menor a 30000, mostrar en pantalla dicho resultado, caso contrario mostrar el mensaje “Gastos por encima de lo presupuestado”.
# historial= (2350, 5960, 23000, 1000, 8900)
# 
# 

# In[2]:


historial= (2350, 5960, 23000, 1000, 8900)
monto_total=0
for i in historial:
      monto_total+=i
if monto_total>30000:
    print("monto total gastado a lo largo del tiempo :",monto_total) 
    print("Gasto por encima de los presupuestado")
else:
    print("El gasto total realizado:",monto_total)
           


# In[ ]:





# In[ ]:



    


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




