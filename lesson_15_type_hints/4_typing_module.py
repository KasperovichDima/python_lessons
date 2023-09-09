from collections import deque  # Что то типа списка (мы этого еще не проходили)
# Импортируем все что нам нужно из модуля typing
from typing import (
    Any,  # Any - абсолютно любой тип данных (что угодно)
    Collection,  # Collection - любая коллекция, которая работает с циклом for
    MutableSequence,  # MutableSequence - изменяемая коллекция
                      # (в которой можно удалять или добавлять элементы)
)


# Задача: Написать функцию, которая принимает любую коллекцию
# и возвращает список из всех элементов коллекции, умноженных на 2.

# Помечаем наш аргумент objects как Collection
# Теперь при попытке вызвать функцию с НЕ колеекцией
# мы получим предупреждение об неправильном типе.
def double(objects: Collection[Any]) -> list[Any]:
    """
    принимает любую коллекцию и возвращает список из
    всех элементов коллекции, умноженных на 2.
    """
    return [el * 2 for el in objects]


print(double('senior'))
print(double((12, 23, 2, 11)))
print(double({12: 12, 'Dima': 36, 'car': 'Mazeratti'}))
print(double([5, 4, False, 'Masha']))
print(double(254))  # Число не является коллекцией. Получаем предупреждение.


# Задача: Написать функцию, которая принимает изменяемую коллекцию
# и убирает из нее все строки.

# Помечаем наш аргумент objects как MutableSequence.
# Теперь при попытке вызвать функцию с НЕизменяемой колеекцией
# мы получим предупреждение об неправильном типе.
def filter_strings(objects: MutableSequence[Any]) -> MutableSequence[Any]:
    ind = 0
    while ind != len(objects):
        if isinstance(objects[ind], str):
            del objects[ind]
            continue
        ind += 1
    return objects


exampe_lst = ['good', 'bad', 34, True, None, 'Dima', 45.7, 'Pavel']
example_deque = deque(['good', 'bad', 34, True, None, 'Dima', 45.7, 'Pavel'])
example_tuple = ('good', 'bad', 34, True, None, 'Dima', 45.7, 'Pavel')  # Кортеж - неизменяемая коллекция

print(filter_strings(exampe_lst))
print(filter_strings(example_deque))
print(filter_strings(example_tuple))  # При передаче кортежа получаем предупреждение.
