import pandas as pd

# Загрузка данных
file_path = 'london.csv'  # Замените на ваш путь к файлу
df = pd.read_csv(file_path)

# Просмотр данных
print(df.head())
print(df.info())

# Преобразуем необходимые столбцы в числовой формат
df['precipitation'] = pd.to_numeric(df['precipitation'], errors='coerce')
df['max_temp'] = pd.to_numeric(df['max_temp'], errors='coerce')
df['mean_temp'] = pd.to_numeric(df['mean_temp'], errors='coerce')
df['min_temp'] = pd.to_numeric(df['min_temp'], errors='coerce')

# Удаляем строки с пропущенными значениями в важнейших столбцах
df_clean = df.dropna(subset=['precipitation', 'max_temp', 'mean_temp', 'min_temp'])

# Проверим информацию о чистых данных
print("\nОбщая информация о чистых данных:")
print(df_clean.info())