import pandas as pd
import numpy as np


chat_id = 682912115 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    a = np.zeros(x.shape[0])
    for i in a:
        a[i] = x[i]*2/70**2
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return a.mean() # Ваш ответ
