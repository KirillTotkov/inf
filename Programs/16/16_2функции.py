# 41)	Алгоритм вычисления функций F(n) и G(n) задан следующими соотношениями:
# 		F(n) = G(n) = 1 при n = 1
# 		F(n) = F(n–1) – 2 · G(n–1), при n > 1
# 		G(n) =  F(n–1) + G(n–1) + n, при n > 1
# Чему равна сумма цифр значения функции G(36)?

from functools import lru_cache    # Мемоизация - запись выисленых занчений функции в кэш
@lru_cache()
def f(n):
    if n==1:
        return 1
    else:
        return f(n-1)-2*g(n-1)
def g(n):
    if n==1:
        return 1
    else:
        return f(n-1)+g(n-1)+n
print(g(36))