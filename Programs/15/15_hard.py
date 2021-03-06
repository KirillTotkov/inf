# (№ 3477) (С.А. Скопинцева) Элементами множества А являются натуральные числа. Известно, что выражение
# ¬((x ∈ {2, 4, 9, 10, 15}) ≡ (x ∈ A)) → ((x ∈ {3, 8, 9, 10, 20}) ≡ (x ∈ A))
# истинно (т.е. принимает значение 1 при любом значении переменной х.
# Определите наименьшее возможное значение произведения элементов множества A.

def f(a,b):
    if a == b:
        return 1
    else:
        return 0

q = set([2,4,9,10,15])
p = set([3,8,9,10,20])

a = set()

for x in range(1,1000):
    m = f(not(x in q), (x in a))
    n = f(x in p, x in a)
    if (m<=n) == 0:
        a.add(x)
print(a)

