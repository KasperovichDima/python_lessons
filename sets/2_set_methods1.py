"""Методы множеств."""
import banks as b
# Создает копию множества.
print(b.has_license.copy())

# Очищает множество.
print(b.has_license)
b.has_license.clear()
print(b.has_license)

# Добавляет элемент в множество
# Помним, что все элементы множества уникальны.
# Если такой элемент уже есть в множестве - оно не изменится.
print(b.support_swift)
b.support_swift.add('JPM')
print(b.support_swift)
b.support_swift.add('BOFA')
print(b.support_swift)

# Удаляет все элементы из множества 1, если они встречаются в множестве 2.
international = {'JPM', 'BOFA', 'USB', 'GSS', 'CPO'}
has_mobile_app = {'BOFA', 'CTGR', 'USB', 'TFC', 'GSS'}
international.difference_update(has_mobile_app)
print(international)

# Удалить элмент из множества.
# Если такого элмента в множестве нет - ничего не произойдет.
b.has_license.discard('PRV')
print(b.has_license)
print(b.has_license)
b.has_license.discard('TFC')
print(b.has_license)

# Удалить элмент из множества.
# Если такого элмента в множестве нет - KeyError.
print(b.has_license)
b.has_license.remove('CTGR')
print(b.has_license)
print(b.has_license)
b.has_license.remove('PRV')


# intersection_update - удалить из множества 1 все элементы,
# которых нет в множестве 2.

print(b.has_mobile_app)
b.has_mobile_app.intersection_update(b.support_swift)
print(b.has_mobile_app)


# .isdisjoint()
# Выводит True, если в обоих множествах нет пересекающихся элементов.
# False - если есть.
s1 = {'JPM', 'CTGR', 'WFC'}
s2 = {'PNC', 'TFC', 'CPO'}
print(s1.isdisjoint(s2))

# s1.issubset(s2) вернет True, если все элементы множества s1 входят в s2.
s2 = {'CTGR', 'WFC', 'PNC', 'TFC', 'PRV'}
s1 = {'CTGR', 'WFC', 'PNC', 'TFC', 'PRV'}
print(s2.issubset(s1))
print(s2.issubset(s1))

# s2.issuperset(s1) вернет True если s2 является суперсетом для s1
# То есть все элементы s1 входят в s2
s1 = {2, 3, 4}
s2 = {1, 2, 3, 4, 5}
print(s2.issuperset(s1))
print(s1.issuperset(s2))

# .pop() извлекает и возвращает первый элемент множества.s2
# если множество пустое - KeyError: 'pop from an empty set'
s2 = {'BOFA', 'CTGR', 'USB', 'TFC', 'GSS'}
print(s2)
print(s2.pop())
print(s2.pop())
print(s2.pop())
print(s2.pop())
print(s2.pop())
print(s2.pop())


# s1.symmetric_difference_update(s2) - в множестве s1 останутся
# только уникальные для обоих множеств элементы.
s1 = {'JPM', 'CTGR', 'WFC'}
s2 = {'JPM', 'BOFA', 'USB', 'GSS', 'CPO'}
s1.symmetric_difference_update(s2)
print(s1)
