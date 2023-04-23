import matplotlib.pyplot as plt

y = ['Java','Python','Php','JS','C#','C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
y_pos=[i for i,_ in enumerate(y)]
plt.barh(y_pos,popularity,color='green')
plt.xlabel('Popularity')
plt.ylabel('Languages')
plt.title('Popularity of Programming Language\n' + 'Worldwide, Oct 2017 compared to a year ago')
plt.yticks(y_pos,y)
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.grid(which='minor',linestyle=':',linewidth='0.5',color='black')
plt.show()
