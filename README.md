# OneHotWithoutGetDummies

Проект демонстрирует, как выполнить one-hot кодирование в DataFrame без использования функции `get_dummies()`.

## Как запустить

1. **Установите pandas**, если он еще не установлен:

   ```bash
   pip install pandas
   ```

2. **Запустите скрипт** `main.py`:

   ```bash
   python main.py
   ```

## main.py

```python
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
```

## Ожидаемый результат

```
    whoAmI  robot  human
0    robot      1      0
1    human      0      1
2    robot      1      0
3    human      0      1
4    robot      1      0
5    robot      1      0
6    human      0      1
7    human      0      1
8    robot      1      0
9    human      0      1
10   robot      1      0
11   human      0      1
12   robot      1      0
13   human      0      1
14   robot      1      0
15   human      0      1
16   robot      1      0
17   human      0      1
18   robot      1      0
19   human      0      1
```

## Краткое описание

- **Что делает скрипт:**
  - Создает DataFrame с одним категориальным столбцом `whoAmI`.
  - Выполняет one-hot кодирование без использования `get_dummies()`.
  - Добавляет новые столбцы для каждой категории с значениями 0 и 1.

- **Как работает кодирование:**
  - Для каждой уникальной категории в столбце `whoAmI` создается новый столбец.
  - В новом столбце ставится 1, если значение в строке соответствует категории, иначе 0.
