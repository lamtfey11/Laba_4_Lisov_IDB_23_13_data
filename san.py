import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных (замените путь на ваш файл)
df = pd.read_csv("london.csv")

# Очистка данных: удаление строк с отсутствующими значениями в интересующих столбцах
df_clean = df[['cloud_cover', 'sunshine']].dropna()

# Группировка данных по уровню облачности и расчёт среднего значения солнечных часов
grouped = df_clean.groupby('cloud_cover')['sunshine'].mean()

# Визуализация: линейный график
plt.figure(figsize=(10, 6))
plt.plot(grouped.index, grouped.values, marker='o', linestyle='-', color='blue')
plt.title('Связь между облачностью и солнечными часами (усреднённые данные)')
plt.xlabel('Облачность (баллы)')
plt.ylabel('Средние солнечные часы (часы)')
plt.grid(True)
plt.tight_layout()

# Рассчитываем корреляцию
correlation = df[['cloud_cover', 'sunshine']].corr()

print("Корреляция между осадками и температурой:")
print(correlation)

plt.show()
