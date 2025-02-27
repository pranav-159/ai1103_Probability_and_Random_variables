# -*- coding: utf-8 -*-
"""Assignment2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13I4uMlGcDfq9Od9k_U8McHUBDJK31uIr
"""

import random

sample_size=10000

blue=0
white=0
red=0
#simulating the picking of marbles from bag
for i in range(sample_size):
  random_variable=random.randint(0,8)
  if random_variable<=2:
    blue+=1
  elif random_variable<=4:
    white+=1
  else:
    red+=1

#calculating the experimental prbability
print("No.of blue marbles picked= {}".format(blue),"\nNo.of white marbles picked= {}".format(white),"\nNo.of red marbles picked= {}".format(red))        
print("Experimental probability and theoritical probability of picking blue= {}--{num:.4f}".format(blue/sample_size,num=3/9))
print("Experimental probability and theoritical probability of picking white= {}--{num:.4f}".format(white/sample_size,num=2/9))
print("Experimental probability and theoritical probability of picking red= {}--{num:.4f}".format(red/sample_size,num=4/9))

#ploting the no.of marbles 
import seaborn as sns
import matplotlib.pyplot as plt

x=["blue","white","red"]
y=[blue,white,red]
sns.barplot(x,y)
plt.show()