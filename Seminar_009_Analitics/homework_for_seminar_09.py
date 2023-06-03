# -*- coding: utf-8 -*-


import pandas as pd
df = pd.read_csv('sample_data/california_housing_train.csv')

#Задача 40: Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)
#df[df['population'] < 500]['housing_medium_value'].mean()

#Задача 42: Узнать какая максимальная households в зоне минимального значения population
df1 = df.loc[df.population < df.population.quantile(.25)]
df1.households.max()