import matplotlib.pyplot as plt
import numpy as np
men_means = [22,30,33,30,26]
women_means = [25,32,30,35,29]

#ax = plt.subplot()
plt.title('Scores by Persons')
plt.xlabel('Person')
plt.ylabel('Scores')


ngroups = 5
x_pos = np.arange(ngroups)
print(x_pos)
opacity=0.8
bar_width=0.35
plt.xticks(x_pos,['G1','G2','G3','G4','G5'])

rect1=plt.bar(x_pos,men_means,bar_width,alpha=opacity,color='red',label='Men')
rect2=plt.bar(x_pos+bar_width,women_means,bar_width,alpha=opacity,color='green',label='Women')

plt.legend()
plt.tight_layout()
plt.show()

