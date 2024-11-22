import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных
file_path = 'londonTemp.csv'  # Укажите путь к вашему файлу
df = pd.read_csv(file_path)

# Преобразуем столбец 'date' в формат datetime
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')

# 2. Визуализация зависимости осадков от температуры
plt.figure(figsize=(12, 6))
plt.scatter(df['precipitation'], df['mean_temp'], alpha=0.5, color='tab:orange')
plt.title('Зависимость осадков от температуры')
plt.xlabel('Осадки (мм)')
plt.ylabel('Средняя температура (°C)')
plt.grid(True)
plt.tight_layout()
plt.show()

# Гипотеза 2: Проверка гипотезы о влиянии осадков на температуру
# Для проверки гипотезы можно вычислить коэффициент корреляции между осадками и температурой
correlation = df[['precipitation', 'mean_temp']].corr()

print("Корреляция между осадками и температурой:")
print(correlation)

# Интерпретация:
# Если коэффициент корреляции близок к -1, то при увеличении осадков температура снижается,
# если близок к 1, то при увеличении осадков температура повышается,
# если близок к 0 — зависимости нет.