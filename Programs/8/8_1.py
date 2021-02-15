# (№ 3540) (Е. Джобс) Женя составляет слова переставляя буквы З, А, П, И, С, Ь.
# Сколько слов может составить Женя, если известно,
# что Ь не может стоять на первом месте и после гласной?

from itertools import *

string="ЗАПИСЬ"
k=0
for p in permutations(string,6):
    s=''.join(p)
    if s[0]!="Ь" and "АЬ" not in s and "ИЬ" not in s:
        k+=1
print(k)