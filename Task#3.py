import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


tips = sns.load_dataset("tips")

#Histogram
sns.histplot(tips['total_bill'], kde=True)
plt.title('Розподіл суми рахунку')
plt.xlabel('Сумa рахунку')
plt.show()


# Boxplot
sns.boxplot(x='day', y='total_bill', data=tips)
plt.title('Порівняння суми рахунку за днями тижня')
plt.xlabel('День тижня')
plt.ylabel('Сума рахунку')
plt.show()

# Scatter Plot
sns.scatterplot(x='total_bill', y='tip', data=tips)
plt.title('Взаимосвязь между суммой счета и размером чаевых')
plt.xlabel('Сума рахунку')
plt.ylabel('Розмір чайових')
plt.show()

# Bar Plot
sns.barplot(x='day', y='total_bill', data=tips, estimator=np.mean)
plt.title('Взаємозв\'язок між сумою рахунку та розміром чайових')
plt.xlabel('День тижня')
plt.ylabel('Сeредня cума рахунку')
plt.show()

# Violin Plot
sns.violinplot(x='time', y='total_bill', data=tips)
plt.title('Розподіл суми рахунку за часом обіду')
plt.xlabel('Час обіду')
plt.ylabel('Сума рахунку')
plt.show()


# Pair Plot
iris = sns.load_dataset("iris")
sns.pairplot(iris, hue='species')
plt.show()
