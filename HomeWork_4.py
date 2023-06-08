# 1. Пользователь вводит с клавиатуры строку. Посчитайте количество букв, цифр в строке. Выведите оба количества
# на экран. (использовать цикл)



name = input("Enter your name: ")
lastName = input("Enter your last name: ")
yearOfBirth = input("Enter your year of birth: ")

letter = 0
numer = 0

for i in name + lastName:
    letter += 1
print(f"Numer of letter: ", letter)

for i in yearOfBirth:
    numer += 1
print(f"Numer of year of birth: ", numer)




# 2. Пользователь вводит с клавиатуры строку и символ для поиска. Посчитайте сколько раз в строке встречается искомый
# символ. Полученное число выведите на экран.
#

line = input("Enter your sentence: ")
symbol = input("Enter your symbol: ")

num = 0

for i in line:
    if i == symbol:
        num += 1
print(f"The symbol is repeated {num} times")



# 3. Пользователь вводит с клавиатуры строку, слово для поиска, слово для замены. Произведите в строке замену одного
# слова на другое. Полученную строку отобразите на экране.


line = input("Enter you sentence: ")
word = input("Enter the word you want to replace: ")
newWord = input("Enter a new word: ")

results = line.replace(word, newWord)
print(results)



# 4. Дана строка. (сделать срезы)
#
# - Сначала выведите третий символ этой строки.
#
# - Во второй строке выведите предпоследний символ этой строки.
#
# - В третьей строке выведите первые пять символов этой строки.
#
# - В четвертой строке выведите всю строку, кроме последних двух символов.
#
# - В пятой строке выведите все символы с четными индексами (считая, что индексация начинается с 0, поэтому символы выводятся начиная с первого).
#
# - В шестой строке выведите все символы с нечетными индексами, то есть начиная со второго символа строки.
#
# - В седьмой строке выведите все символы в обратном порядке.
#
# - В восьмой строке выведите все символы строки через один в обратном порядке, начиная с последнего.
#
# - В девятой строке выведите длину данной строки.

sentence = "Things don't always work out the first time"
results = sentence[2:3]
print(results)
results = sentence[0:5]
print(results)
results = sentence[0:-2]
print(results)
results = sentence[0::2]
print(results)
results = sentence[1::2]
print(results)
results = sentence[::-1]
print(results)
results = sentence[::-2]
print(results)
results = len(sentence)
print(results)