import matplotlib.pyplot as plt
import numpy as np

men_means=[22,30,35,35,26]
women_means=[25,32,30,35,29]
men_std=[4,3,4,1,5]
women_std=[3,5,2,3,3]
N = 5
index=np.arange(N)

m = plt.bar(index,men_means,width=0.35,color='red',yerr=men_std,label="Men")
w = plt.bar(index,women_means,width=0.35,color='green',bottom=men_means,yerr=women_std,
            label="Women")
plt.legend()
plt.xlabel('Groups')
plt.ylabel('Scores')
plt.xticks(index,['Group1','Group2','Group3','Group4','Group5'])
plt.title('Scores by group and gender')
plt.show()
