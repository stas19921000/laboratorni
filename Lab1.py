#1 оголошення змінних та типи даних
    #1.1 оголшення змінних
a = 2
b = 3.7
c = "hello"
d = True
    #1.2 вивід та тип змінних 
print (a)
print (b)
print (c)
print (d)
print (type(a))
print (type(b))
print (type(c))
print (type(d))

#2 операції з числами
    #2.1 використання простихарифматематичних операцій
print (a + b)
print (a - b)
print (a * b)
print (a / b)
print (a ** b)

    #2.2 використання функцій та оператора %
print (abs(-a))
print (round(b))
print (a % b)

    #2.3 знаходимо середнє арифметичне з трьох чисел
e = 33
print ((a + b + e) / 3)

#3 робота з рядками
    #3.1 створюємо рядкову змінну
text = "Стас"
text2 = "Тест"

    #3.2 використовуємо методи роботи з рядкоми
print (text.upper())
print (text.lower())
print (text + text2)

    #3.3 виводимо на екран рядок, що містить ім'я та вік
print ("{} {}".format(text, e))

#4 умовні конструкції
    #4.1 перевіряємо чи введене користувачем число парне
num = int(input("Введіть число: "))
if num % 2 == 0:
    print ("Число", num, "парне")
else:
    print ("Число", num, "непарне")
    #4.2 перевіряємо чи введене користувачем входить в діапазон від 10 до 50
    # if, elif, else
if num < 10:
    print ("Число", num, "менше 10")
elif num > 50:
    print ("Число", num, "більше 50")
else:
    print ("Число", num, "входить в діапазон від 10 до 50")
    # або використовуємо логічний оператор and
    print ("Варіант 2 використовуємо логічний оператор and")
if num >= 10 and num <= 50:
    print ("Число", num, "входить в діапазон від 10 до 50")
else:
    print ("Число", num, "не входить в діапазон від 10 до 50")
    
#5 Цикли 
    #5.1 використовуємо цикл for який виводить цифри від 1 до 10
for i in range(1, 11):
    print(i)
    #5.2 використовуємо цикл while який виводить cумму чисел від 1 до 100 
sum = 0
i = 1
while i <= 100:
    sum += i
    i += 1
print(sum)

 #6 Функції
    #6.1 напишемемо функцію що приймає два числа і повертає їх суму
a = int(input("Введіть число: "))
b = int(input("Введіть число: "))
def sum(a, b):
    return a + b
print(sum(a, b))
    #6.2 створюємо функцію, що приймає рядок і повертає його у зворотному порядку
def zvorot(text):
    return text[::-1] # читаємо текст у зворотному порядку
print(zvorot(text))

#7 Списки і цикли
    #7.1 створюємо списки із 5 чисел
numbers = [1, 2, 3, 4, 5]
    #7.2 цикл який виводить на екран елементи списку
for i in numbers:
    print(i)
    #7.3 додаємо новий елемент до списку та видаляємо останній
numbers.append(6) #або numbers.append(порядок числа в рядку з початку, число)
numbers.pop() #або numbers.pop(число з кінця) або del numbers[число з початку]
print(numbers)

#8 робота з словниками
    #8.1 створюємо словник, що містить дані студента ім'я, вік та факультет
student = {"ім'я": "Стас", "вік": 18, "факультет": "Комп'ютерні науки"}
    #8.2 виводимо на екран дані студента з ключами
print(student)
    #8.3 додаємо новий ключ "рік навчання" та присвоюємо йому значення
student["рік навчання"] = int(input("Введіть рік навчання: "))
print(student)
#9 обробка виключень try-except
    #9.1 пишемо програму з запитом двох чисел та діленням першого на друге
    a = int(input("Введіть перше число: "))
    b = int(input("Введіть друге число: "))
    print(a / b)
    #9.2 тепер пишемо програму використовуючи try-except для обробки виключення ділення на нуль
try:
    a = int(input("Введіть перше число: "))
    b = int(input("Введіть друге число: "))
    print(a / b)
except ZeroDivisionError:
    print("На нуль ділити не можна")