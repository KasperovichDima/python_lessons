"""Также у множеств есть 'знаковые' методы."""
import banks as b


# & - пересечение. То есть элементы, которые есть и в одном
# и во втором множестве. Если в одном множестве элемент есть,
# а в другом нет - он не попадет в результат.

# Найти банки, которые международные И имеют лицензию:
print(b.international & b.has_license)
# То же самое что set1.intersection(set2)
print(b.international.intersection(b.has_license))


# | - объединение. То есть элементы, которые
# есть либо в первом либо во втором множестве.

# Найти банки, которые имеют мобильное
# приложение ИЛИ подключены к SWIFT:
print(b.support_swift | b.has_license)
# То же самое что set1.union(set2)
print(b.support_swift.union(b.has_license))


# Знаком - мы вычитаем одно множество из другого.
# То есть результатом будут все элементы первого множества,
# кроме тех, которые есть во втором.

# Найти банки подключены к SWIFT но у них нет лицензии:
print(b.support_swift - b.has_license)
# То же самое что set1.difference(set2)
print(b.support_swift.difference(b.has_license))


# ^ - получить разность двух множеств.
# То есть получить элементы, которых нет в 2 множествах одновременно.

# Найти банки, у которых нет лицензии или они не подключены к SWIFT.
print(b.support_swift ^ b.has_license)
# То же самое что set1.symmetric_difference(set2)
print(b.support_swift.symmetric_difference(b.has_license))
