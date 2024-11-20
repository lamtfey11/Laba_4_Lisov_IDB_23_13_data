import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных
file_path = 'london_weather.csv'  # Замените на ваш путь к файлу
df = pd.read_csv(file_path)

# Просмотр данных
print(df.head())
print(df.info())