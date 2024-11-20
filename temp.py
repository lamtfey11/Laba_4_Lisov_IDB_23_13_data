import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных
file_path = 'londonTemp.csv'  # Укажите путь к вашему файлу
df = pd.read_csv(file_path)

# Преобразуем столбец 'date' в формат datetime
df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')

# 1. Визуализация зависимости температуры от даты
plt.figure(figsize=(12, 6))
plt.plot(df['date'], df['mean_temp'], label='Средняя температура', color='tab:blue')
plt.title('Зависимость температуры от даты')
plt.xlabel('Дата')
plt.ylabel('Температура (°C)')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()