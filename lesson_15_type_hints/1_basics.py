int  # Целое число. Пример 165 или -3
float  # Дробное число. Пример -45.054 или 7.85
bool  # Булево значение Пример True или False
str  # Строка. Пример 'Odessa'
list  # Список значений. Пример ['Klim', 'Mark', 'Artem'] или [4, 6, 8]
tuple  # Кортеж значений. Пример ('a', 'b', 'c') или (17, 23, 36)
dict  # Словарь, содержащий пары ключ-знаечние. Пример {'car': 'Mercedes', 'pen': 'Parker'}
None  # Отсутствие значения или пустое значение.


x: int  # Объявление типа
x = 15  # Инициализация
x: int = 15  # Объявление типа + Инициализация

x = 'Odessa'  # Красным подчеркнута ошибка типа

print(x)  # Тем не менее такой код будет работать.
