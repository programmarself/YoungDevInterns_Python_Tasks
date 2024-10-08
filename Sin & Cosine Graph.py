# -*- coding: utf-8 -*-
"""Sin_and_Cosine_graph.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Iht2bw9CagukXVYfn4OL4PzT6YVomjRV

# **Sine and Cosine Graph Using MatplotLib Module**

<h2 style="font-family: 'poppins'; font-weight: bold; color: Green;">👨💻 Author: Irfan Ullah Khan</h2>

[![GitHub](https://img.shields.io/badge/GitHub-Profile-blue?style=for-the-badge&logo=github)](https://github.com/programmarself)
[![Kaggle](https://img.shields.io/badge/Kaggle-Profile-blue?style=for-the-badge&logo=kaggle)](https://www.kaggle.com/programmarself)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=for-the-badge&logo=linkedin)](https://www.linkedin.com/in/irfan-ullah-khan-4a2871208/)  

[![YouTube](https://img.shields.io/badge/YouTube-Profile-red?style=for-the-badge&logo=youtube)](https://www.youtube.com/@irfanullahkhan7748)
[![Email](https://img.shields.io/badge/Email-Contact%20Me-red?style=for-the-badge&logo=email)](mailto:programmarself@gmail.com)
[![Website](https://img.shields.io/badge/Website-Contact%20Me-red?style=for-the-badge&logo=website)](https://flowcv.me/ikm)

# Import Libraries
"""

import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0,4*np.pi,0.1)
y=np.sin(x)

plt.plot(x,y)
plt.show()

x=np.arange(0,4*np.pi,0.1)
y=np.sin(x)
z=np.cos(x)

plt.plot(x,y,z)
plt.show()

x=np.arange(0,4*np.pi-1,0.1)
y=np.sin(x)
z=np.cos(x)

plt.plot(x,y,z)
plt.xlabel('x values form 0 to 4pi')
plt.ylabel('sin(x) and cos(x)')
plt.title('Plot of sin and cos from 0 to 4pi')
plt.legend(['sin(x)','cos(x)'])
plt.show()

t=[0,30,45,60,90]
x=[i*(np.pi/180) for i in t]
plt.plot(x,np.sin(x),marker="+")
plt.plot(x,np.cos(x),marker="^")
plt.show()

"""#  Adding degree to the graph"""

t=[0,30,45,60,90]
x=[i*(np.pi/180) for i in t]
plt.plot(t,np.sin(x),marker="+")
plt.plot(t,np.cos(x),marker="^")
plt.xticks(t)
plt.show()

"""# Adding the title and the labels"""

t=[0,30,45,60,90]
x=[i*(np.pi/180) for i in t]
plt.plot(t,np.sin(x),marker="+")
plt.plot(t,np.cos(x),marker="^")
plt.xticks(t)
plt.title("Sin and Cos Graph")
plt.xlabel("Angel")
plt.ylabel("Sin and Cos Value")
plt.show()

"""# Adding the legend"""

t=[0,30,45,60,90]
x=[i*(np.pi/180) for i in t]
plt.plot(t,np.sin(x),marker="+",label="sin")
plt.plot(t,np.cos(x),marker="^",label="cos")
plt.xticks(t)
plt.title("Sin and Cos Graph")
plt.xlabel("Angel")
plt.ylabel("Sin and Cos Value")
plt.legend()
plt.show()

"""# Differnt Graph"""

t=np.linspace(-np.pi,np.pi)
plt.plot(t,np.sin(t),marker="+",label="sin")
plt.plot(t,np.cos(t),marker="^",label="cos")

plt.title("Sin and Cos Graph")
plt.xlabel("Angel")
plt.ylabel("Sin and Cos Value")
plt.legend()
plt.show()

"""# Another graphc"""

t=np.arange(0,4*np.pi,0.5)
plt.plot(t,np.sin(t),marker="+",label="sin")
plt.plot(t,np.cos(t),marker="^",label="cos")

plt.title("Sin and Cos Graph")
plt.xlabel("Angel")
plt.ylabel("Sin and Cos Value")
plt.legend()
plt.show()