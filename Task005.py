#Английский словарь
#"Пора учить английский язык", - сказал себе Степа 
# и решил написать программу для изучения английского языка. 
# Программа получает на вход слово на английском языке и 
# несколько его переводов на русском языке. 
# Составьте словарь, в котором ключ - это английское слово, 
# а значение - это список русских слов. В этой задаче нужно использовать строчный метод split().

n = int(input('Количество слов - '))
words_dict = {}
for _ in range(n):
    words = input().split()
    for i in range(len(words)):
        if words[i] == '-':
            j = words[i - 1]
            temp = list(words[i + 1:])
            words_dict[j] = temp
            break
print(words_dict)
