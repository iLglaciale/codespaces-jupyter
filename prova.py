# %% [markdown]
# ## Esempio di notebook

# %%
import math

from math import acos as arcos

from math import log10 as log

from math import log as ln

import numpy as np

import matplotlib.pyplot as plt






# %%
math.sin(1)

print("log(10) =",log(10))

print("math.log = ln")

print("loge(10) =",ln(10))

m=5.3

print("pi greco =",math.pi)

print("massa =",m,"kg")


# %% [markdown]
# ## ESEMPI CON NUMPY

# %%
a=np.array([1,2,3])

print(a)
print(a+1)

x=np.linspace(0,10,10)

y=3*x+2
print("x =",x)
print("y =",y)

b=np.array([[1,2,3],[4,5,6]])
print("b =",b)

z=np.zeros(11)

print(z)
z[3]=69
z[10]=70
z[0]=420
print(z)
az=np.zeros_like(b)
print(az)

# %% [markdown]
# ## ESEMPI CON MATPLOTLIB

# %%
x=np.linspace(0,2*np.pi,1000) # mille valori nell'intervallo [0,2pi]
y=np.sin(x)
z=np.cos(x)

plt.plot(x,y,x,z)
plt.grid() # griglia
plt.plot(x,y*np.exp(-x))
plt.show() # non necessario in jupiter notebooks

