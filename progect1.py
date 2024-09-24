import string
import itertools

passwordReal = "3333"  # пароль, который нужно подобрать

# Множество символов, которые будем использовать для подбора (только цифры)
guessPasswordSet = string.digits  # Замените на string.digits + string.ascii_letters + string.punctuation, если нужно
guessPasswordLength = 1  # начальная длина пароля для подбора
maxPasswordLength = 4  # максимальная длина пароля для подбора

# Функция, которая создает все возможные комбинации символов заданной длины
def stringIter(chars, length):
    yield from itertools.product(chars, repeat=length)  # генерация комбинаций символов

# Цикл для перебора паролей
while guessPasswordLength <= maxPasswordLength:  # Добавляем условие на максимальную длину
    # Перебираем все возможные комбинации символов длиной guessPasswordLength
    for passwordSet in stringIter(guessPasswordSet, guessPasswordLength):
        passwordString = ''.join(passwordSet)  # превращаем кортеж символов в строку
        if passwordString == passwordReal:  # если текущий пароль совпал с реальным
            print("Password is found: ", passwordString)  # выводим найденный пароль
            exit()  # завершаем программу
    # Увеличиваем длину пароля, если совпадение не найдено
    guessPasswordLength += 1

print("Password not found within the specified length.")
