"""Овощной магазин с хамским обслуживанием."""
import random
from utils import print_price_list
from price import price_list


print('Добро пожаловать в магазин "Гнилое Яблоко"!')
# TODO: Когда мы запрашиваем у клиента, сколько он готов потратить,
# клиент может ввести не число, а, например, строку, или просто нажать Enter
# Или ввести отрицательное число. Нужно как то эту проблему решить.
# Подумайте над решением. Подсказка - нужно исользовать цикл while.
clients_money = float(input('Деньги есть?!! А если найду? Сколько есть?\n'))  # TODO: Add type hint
cart = {}  # TODO: Add type hint
while sum(cart.values()) < clients_money:  # Пока сумма покупок < количеству денег у клиента
    print_price_list()
    # TODO: Тут тоже могут быть проблемы. Клиент может написать название
    # товара с маленькой буквы, или ошибиться и ввести товар которого нет в
    # нашем прайс-листе. Подумайте, как мы можем проверить и предварительно
    # обработать ввод клиента. Как потом мы можем проверить есть ли такой
    # товар в нашем прайс листе и как сообщить клиенту, если такого товара у
    # нас в магазине нет.
    product = input('Слышь, чё брать то будешь?\n')  # TODO: Add type hint
    if not product:
        break
    # TODO: И тут нас могут ждать непприятные сюрпризы. Что если клиент введет
    # 0 или отрицательное значение или вообще не число. Что мы будем делать
    # в этом случае.
    weight = float(input('Сколько кило?\n'))  # TODO: Add type hint
    # Проверяем, что денег у него достаточно чтобы добавить этот товар в корзину
    new_cart_sum = sum(cart.values()) + price_list[product] * weight
    if clients_money >= new_cart_sum:  # Если денег хватает, то
        cart[product] = price_list[product] * weight  # Добавляем товар в корзину
    else:
        print(f'Тебе не хватает {new_cart_sum - clients_money}')

    print(f'Ты уже набрал тут на {sum(cart.values())}.')

print('\n')
print(f'Фискальный чек номер {random.randint(10_000, 99_999)}')
for product, coast in cart.items():
    print(f'{product}........{coast} долларов.')
print(f'Сумма покупок {sum(cart.values())}.')
print('\n')
print(f'Ваша сдача {clients_money - sum(cart.values())}. Забирай и проваливай!')
print('\n')
print('СЛЕДУЮЩИЙЙЙ!!!')
