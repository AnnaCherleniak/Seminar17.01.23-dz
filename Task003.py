#3. Старший и младший
#Пользователь вводит число N. 
# Затем он вводит личные данные (имя и возраст) своих N друзей. 
# Создайте список friends и добавьте в него N словарей с ключами name и age. 
# Найдите самого младшего из друзей и выведите его имя.
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
print(friends_list)
print(f'{age_dict[min(age_dict)]} самый младший из друзей')