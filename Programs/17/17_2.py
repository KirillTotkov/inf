# 25)	(А. Куканова) Рассматривается множество целых чисел,
# принадлежащих числовому отрезку [3672; 9117],
# которые удовлетворяют следующим условиям:
# − остаток от деления на 3 равен 2;
# − остаток от деления на 5 равен 4.
# Найдите количество таких чисел и их сумму.
# Гарантируется, что искомая сумма не превосходит 10**7.

def isGoodNumber(i):
    return i % 3==2 and i%5==4

a=[i for i in range(3672,9118) if isGoodNumber(i)]
print(len(a),sum(a))