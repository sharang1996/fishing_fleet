#!/usr/bin/env python
# coding: utf-8

# 

# ## Abstract
# 
# The data set records data for a time period of one day during which one fisherman has fished in a lake. The fisherman uses three types of fishing rods, labeled A, B, and C, each using different bait. The fisherman has
# recorded every catch he has made during this time. The data set consists of three columns with X values giving the times at which the fisherman has made a catch, the Y values indicate the size of that catch (i.e. its weight in kg), and the Z values give a letter A, B, or C which indicates which fishing rod was used to make that catch. 

# 

# ## Importing necessary libraries, loading and cleaning data

# In[69]:


import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import spearmanr


# In[33]:


rows = open('fish1.txt').read().split('\n')


# In[34]:


del rows[-1]
X=[]
Y=[]
Z=[]


# In[35]:


for row in rows:
    cols = row.split()
    X.append(float(cols[0]))
    Y.append(float(cols[1]))
    Z.append(cols[2])


# 

# # Task 1

# 

# ## Plot for mapping time of catch in the day against its frequency

# In[68]:


mean = np.mean(X)
median = np.median(X)
std = np.std(X)

print("Median timing : "+str(median) + " hour of the day")
print("Mean timing : "+str(mean) + " hour of the day\n")
print("Mean is to the right of the median, and hence we have a right skewed distribution as clearly visible in the plot.\n")
print("standard deviation : "+str(std))

min_range = (mean - 2*std)

if min_range<0:
    min_range=0
    
max_range = (mean + 2*std)

print("\nMean range for 95% confidence interval(+- 2 standard deviations) : " + str(min_range) + " to " + str(max_range))

plt.hist(X)
plt.title("catches against hour of the day")
plt.xlabel("time of catch(24 hour distribution)")
plt.ylabel("frequency of catch")
plt.show()


# 

# ## Plot for mapping frequency for various catch sizes 

# In[58]:


mean = np.mean(Y)
median = np.median(Y)
std = np.std(Y)

print("Median catch size(kgs) : "+str(median))
print("Mean catch size(kgs) : "+str(mean))
print("\nMean is to the right of the median, and hence we have a right skewed distribution as clearly visible in the plot.\n")
print("standard deviation : "+str(std))


min_range = (mean - 2*std)

if min_range<0:
    min_range=0
    
max_range = (mean + 2*std)

print("\nMean range for 95% confidence interval(+- 2 standard deviations) : " + str(min_range) + " to " + str(max_range))

ar=np.array(Y)
plt.hist(gn.astype('float'))
plt.title("catches for various sizes")
plt.xlabel("size of catch(kgs)")
plt.ylabel("frequency of catch")
plt.show()


# 

# ## Plot for comparing the types of baits and frequency of catches against each bait

# In[38]:


plt.hist(Z)
plt.title("catches against bait type")
plt.xlabel("type of bait")
plt.ylabel("frequency of catch")
plt.show()


# 

# ## Findings from task 1

# From the above plots, we can draw certain inferences : 
# 1. Early hours of the day yield more fish, and it steadily starts decreasing in the afternoon, from around 1 PM.
# 2. Most of the catch weighs less than 3 kgs, very few weigh well over it
# 3. Bait type C has the most catches associated against it

# 

# # Task 2

# ## Analyse the dependence between time of catch, size of catch, and the type of bait used

# 

# ## Catch size against time of the day

# In[70]:


fig, ax = plt.subplots(figsize=(10, 6))

ax.scatter(x = X, y = Y)
plt.xlabel("Timing of the day(in hours of day)")
plt.ylabel("Catch size(kgs)")

plt.show()

# calculate spearman's correlation
corr, _ = spearmanr(X, Y)
print('Spearmans correlation: %.3f' % corr)


# As we can see from the plot above, there is a correlation between the catch size and time of the day, and as its negative, it implies that earlier timings yield larger catch sizes

# 

# ## Catch size against Bait type

# In[74]:


fig, ax = plt.subplots(figsize=(10, 6))

ax.scatter(x = Z, y = Y)
plt.xlabel("Bait Type")
plt.ylabel("Catch size(kgs)")

plt.show()


# In[77]:


print(Z.count('A'))
print(Z.count('B'))
print(Z.count('C'))


# As we can see above, Bait type C is associated with the largest number of catches, and is the most used type of bait. We cannot surely conclude if C is more effective, and hence is used more, or if it has large catches by the sheer frequency of its use as compared to the rest. 

# 

# ## Bait type against time of the day

# In[73]:


fig, ax = plt.subplots(figsize=(10, 6))

ax.scatter(x = X, y = Z)
plt.xlabel("time of the day")
plt.ylabel("Bait Type")

plt.show()


# From the above plot, we can infer that bait type A is used more frequently in the early hours of the day, and bait type C is used less frequently in the latter end of the day. Bait type B seems to be used much less frequently, and more distributed, as compared to the other 2. at 15:00, or 3 PM, bait type C seems to be the more frequently used bait type.

# 

# ## 3D scatter plot depicting all the 3 axis, and their relation.

# In[66]:


from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
    
z_transformed = [ord(z)-65 for z in Z]

ax.scatter(X, Y, z_transformed)
ax.set_xlabel("Timing of the day(in hours of day)")
ax.set_ylabel("Catch size(kgs)")
ax.set_zlabel("Bait Type 0 : A, 1 : B, 2 : C")

plt.show()


# 

# # Conclusion

# 1. Best time to go fishing is from 2:30AM to 5:00AM
# 2. Bait associated with most catches : Bait C
# 3. Best bait type at 3PM : Bait C
