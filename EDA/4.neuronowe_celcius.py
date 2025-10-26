import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('f-c.csv', usecols = [1, 2])
print(df.head(3))

from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(df[['F']], df.C)
print(f'Współczynnik kierunkowy: {model.coef_}\nWyraz wolny: {model.intercept_}')

plt.scatter(df.F, df.C)
plt.plot(df.F, df.F * model.coef_ + model.intercept_, c = 'r')
plt.show()
