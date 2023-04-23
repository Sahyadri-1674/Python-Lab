import matplotlib.pyplot as plt

languages = ['Java','Python','PHP','JavaScript','C#','C++']
popularity = [22.4,17.6,8.8,7.7,6.7,6.6]
explode=(0.1,0,0,0,0,0)
plt.pie(popularity,explode=explode,labels=languages,shadow=True,startangle=140)
plt.title('Popularity of Programming languages\n'+"Worldwide,Oct 2022 compared to a year ago")
plt.show()
