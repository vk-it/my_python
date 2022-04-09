#print("Hello")
#print("Hello '\"' world!")
#print(2+3)
#print("Hello,", "Alex", "and Michael", sep="abc")
#print("Hello, \nAlex")
#print("Я прохожу курс \nпо Python")
#print("Я учу Python по курсу: \n‘Программирование на Python с Нуля до Гуру’")
#print("Я прохожу курс по Python\nЯ учу Python по курсу: ‘Программирование на Python с Нуля до Гуру’" )

#age = 25
#print(age)
#print("Возраст: " + str(age))
#print("Возраст:", age)
#temp = 5.9 #в программирование десятичная через точку
#print("Температура", temp, "градусов")

#username = "Alex"
#print("Имя пользователя:", username); print("Имя пользователя:", username)

#isexists = True
#print("Существует:", isexists)
#isexists = False
#print("Существует:", isexists)

#age = "18.5"
#print("Возраст: " + age)

#print("Тип переменной age: ", type(age))
#print("Тип переменной temp: ", type(temp))
#print("Тип переменной username: ", type(username))
#print("Тип переменной isexists: ", type(isexists))
#print("Тип переменной integer: ", type(10))

#number = 10
#print(number)
#number = 15
#print("Значение переменной number равно", number)

#str1 = "Значение переменной"
#str2 = "равно"
#print(str1, "number", str2, number)

#first = True
#two = False
#print(str1, "first", str2, first, str1, "two", str2, two)

#int = 10 #Присваивание переменной int
#print(int) #Вывод переменной int
#int = 15 #Присваивание переменной int
#print("Значение переменной int = " + str(int)) #Вывод переменной и определение типа int
#abc = "Hello" #Присваивание переменной str
#print("Значение переменной abc = " + abc) #Вывод переменной str
#cba = "Word" #Присваивание переменной str
#print("Значение переменной cba = " + cba) #Вывод переменной str

#hello = True #Присваивание переменной bool
#bye = False #Присваивание переменной bool
#print("Значение переменной hello = ", type(hello)) #Вывод переменной и определение типа bool
#print("Значение переменной bye = ", type(bye)) #Вывод переменной и определение типа bool

#text = '''Первая строка
#Вторая строка
#Третья строка'''
#print(text)

'''
Выводим тип переменной
Это строка, НЕ комментарий, но можно использовать так,
так как не присваивается переменная
'''

x = 3
y = 8
print("x + y =", x + y)
print("x - y =", x - y)
print("x * y =", x * y)
print("(x % y) ** x =", (x % y) ** x)
print("(x % y) ** y =", (x % y) ** y)
#print((15 * 10 - 20) / 2) + 14 * 10 + (-45)
print(int((15 * 10 - 20) / 2) + 14 * 10 + (-45))
x = 10
print(bin(x))