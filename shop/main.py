"""Овощной магазин с хамским обслуживанием."""
import random
from utils import print_price_list
from price import price_list


print('Добро пожаловать в магазин "Гнилое Яблоко"!')
clients_money = float(input('Деньги есть?!! А если найду? Сколько есть?\n'))
cart = {}
while sum(cart.values()) < clients_money:  # Пока сумма покупок < количеству денег у клиента
    print_price_list()
    product = input('Слышь, чё брать то будешь?\n')  # Запрашиваем у покупателя название продукта, который он хочет добавить в корзину
    if not product:
        break
    weight = float(input('Сколько кило?\n'))  # Запрашиваем сколько килограмм
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
