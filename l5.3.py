# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb



# импортировали датасет
df = pd.read_csv('test.csv')
# взяли 1000 значений
df_sample = df.sample(1000)
# проверка данных на пропуски
missing_values = df_sample.isnull().sum()
print("Пропуски в данных: ")
print(missing_values)
#проверяем на выбросы
fig, axes = plt.subplots(1, 2, figsize=(12, 5))
#ящик с усами
sb.boxplot(data=np.log1p(df_sample['Square']), ax=axes[0].axes)
axes[0].set_title('Ящик с усами (логарифмическая шкала)')
# гистограмма
sb.histplot(data=np.log1p(df_sample['Square']), ax=axes[1], bins=30, kde=True)
axes[1].set_title('Гистограмма (логарифмическая шкала)')
plt.show()
#заполняем пропуски средним значением
# Заполняем пропуски в столбце 'LifeSquare' средним значением
df_sample['LifeSquare'].fillna(df_sample['LifeSquare'].mean(), inplace=True)

# Заполняем пропуски в столбце 'Healthcare_1' средним значение
df_sample['Healthcare_1'].fillna(df_sample['Healthcare_1'].mean(), inplace=True)


# Определяем количество квартир по количеству комнат
room_counts = df_sample['Rooms'].value_counts()
print("Количество квартир по количеству комнат:")
print(room_counts)
# Сводная таблица
pivot_table = pd.pivot_table(df_sample, values='Id', index='DistrictId', columns='Rooms', aggfunc='count', fill_value=0)
print("\nСводная таблица:")
print(pivot_table)
