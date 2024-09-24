Python 3.12.6 (tags/v3.12.6:a4a2d2b, Sep  6 2024, 20:11:23) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import string
... import itertools
... 
... passwordReal = "3333"  # пароль, который нужно подобрать
... 
... # Множество символов, которые будем использовать для подбора (цифры, буквы, знаки пунктуации)
... guessPasswordSet = string.digits + string.ascii_letters + string.punctuation
... guessPasswordLength = 1  # начальная длина пароля для подбора
... maxPasswordLength = 4  # максимальная длина пароля для подбора
... 
... # Функция, которая создает все возможные комбинации символов заданной длины
... def stringIter(chars, length):
...     yield from itertools.product(chars, repeat=length)  # генерация комбинаций символов
... 
... # Цикл для перебора паролей
... while guessPasswordLength <= maxPasswordLength:  # Добавляем условие на максимальную длину
...     # Перебираем все возможные комбинации символов длиной guessPasswordLength
...     for passwordSet in stringIter(guessPasswordSet, guessPasswordLength):
...         passwordString = ''.join(passwordSet)  # превращаем кортеж символов в строку
...         if passwordString == passwordReal:  # если текущий пароль совпал с реальным
...             print("Password is found: ", passwordString)  # выводим найденный пароль
...             exit()  # завершаем программу
...     # Увеличиваем длину пароля, если совпадение не найдено
...     guessPasswordLength += 1
... 
... print("Password not found within the specified length.")
... Type "help", "copyright", "credits" or "license()" for more information.
SyntaxError: multiple statements found while compiling a single statement
