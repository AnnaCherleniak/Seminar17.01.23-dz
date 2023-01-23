# 1.Создайте список из случайных чисел. Найдите количество различных элементов в нем.
from random import randint

some_list = [randint(1, 20) for _ in range(20)]
print(some_list)
# 1ый вариант
new_list = set(some_list)
print(len(new_list))
# 2ой вариант
new_list = set()
for e in some_list:
    if e not in new_list:
        new_list.add(e)
print(len(new_list))