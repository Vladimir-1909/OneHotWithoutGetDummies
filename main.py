import pandas as pd
import random

# Создаем список с данными
lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)

# Создаем DataFrame
data = pd.DataFrame({'whoAmI': lst})

# One-hot кодирование без get_dummies()
for category in data['whoAmI'].unique():
    data[category] = (data['whoAmI'] == category).astype(int)

# Выводим результат
print(data)
