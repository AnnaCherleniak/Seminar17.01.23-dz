#2.  Фрукты
#Пользователь вводит число K - количество фруктов. 
# Затем он вводит K фруктов в формате: название фрукта и его количество. 
# Добавьте все фрукты в словарь, где название фрукта - это ключ, а количество - значение. 

k = int(input('количество фруктов: '))
some_dict = {}
for i in range(k):
    j = input('фрукт: ')
    some_dict[j] = int(input('количество этого фрукта: '))
print(some_dict)