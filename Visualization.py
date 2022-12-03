#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df=pd.read_csv("pima-indians-diabetes.csv")
df.head()


# In[3]:


df.describe()


# In[4]:


df=df[df["BMI"]!=0]
df1=df.copy()
for col in df1.columns[1:7]:
    df1[col]=df1[col].replace(0,np.nan)
df1.head()
df1.describe()


# In[5]:


#checking for normality of the variables
plt.figure()
for i, col in enumerate(df1.columns[1:7]):
    sns.displot(df1[col],kde=True)
plt.show()


# In[22]:


#visual of possible correlation between variables
sns.pairplot(df,kind="reg",diag_kind="kde")


# In[8]:


plt.figure(figsize=(8,8))
mycolors=["red","blue"]
result=list(set(df1["diabetes"]))
for i in result:
    data=df.loc[df1["diabetes"]==i]
    plt.scatter(data["times_pregnant"],
                data["plasma_glucose_concentration"],
                label=i,
                s=20,
                c=mycolors[i])
plt.xlabel("Times Pregnant")
plt.ylabel("Plasma glucose Concentration")
plt.title("Plasma Glucose Conntration vs Times Pregnant")
plt.legend()
plt.show()


# In[9]:


plt.figure(figsize=(8,8))
mycolors=["hotpink","blue"]
for i in result:
    data=df.loc[df1["diabetes"]==i]
    plt.scatter(data["times_pregnant"],
               data["BMI"],
               label=i,
               s=50,
               c=mycolors[i])
plt.xlabel("Times Pregnant")
plt.ylabel("BMI")
plt.title("BMI VS TIMES PREGNANT")
plt.legend()
plt.show()


# In[10]:


fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(111, projection='3d')
mycolors =["red","blue"]
for i in result:
    data=df1.loc[df1["diabetes"]==i]
    ax.scatter(data["age"],
                data["times_pregnant"],
                data["plasma_glucose_concentration"],
                label=i,
               c=mycolors[i],
                s=50,
               zdir="z")
angle=45
plt.xlabel("Age")
plt.ylabel("Times Pregnant")
ax.set_zlabel("Plasma glucose Concentration",rotation=angle)
plt.title("3D plot showing Age vs Times Pregnant vs Plasma Glucose Concentration")
plt.legend()
plt.show()


# In[15]:


df2=df1.loc[df1["age"]>=35]
df2.head()


# In[18]:


sns.jointplot(data=df2,x=df2["age"],
             y="diastolic_blood_pressure",
             hue=df2["diabetes"],
             s=50,
             palette="deep")


# In[21]:


sns.jointplot(data=df2,x=df2["BMI"],
             y="diastolic_blood_pressure",
             hue=df2["diabetes"],
             s=100,
            alpha=0.5,
             palette="cool")


# In[ ]:




