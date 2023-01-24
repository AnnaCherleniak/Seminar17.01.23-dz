#4.  Еще немного о друзьях
#Пользователь вводит число N. 
# Затем он вводит личные данные (имя и возраст) своих N друзей. 
# Создайте список friends и добавьте в него N словарей с ключами name и age. 
# Выведите средний возраст всех друзей и самое длинное имя.
from statistics import mean

n = int(input('введите количество друзей: '))
friends_list = []
name_dict = {}
age_dict = {}
for _ in range(n):
    i = input('имя: ')
    j = int(input('возраст: '))
    name_dict[i] = j
    age_dict[j] = i
friends_list.append(name_dict)
friends_list.append(age_dict)
print(f'Средний возраст друзей = {round(mean(age_dict))}')
temp_max = 0
for name in name_dict.keys():
    if len(name) > temp_max:
        temp_max = len(name)
        name_max = name
print(f'Самое длинное имя - {name_max}')