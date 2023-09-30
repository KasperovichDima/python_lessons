"""Овощной магазин с хамским обслуживанием."""
import utils as u


print('Добро пожаловать в магазин "Гнилое Яблоко"!')

clients_money = u.get_clients_money_amount()

u.start_byuing_process(clients_money)
u.print_receipt()
u.get_change(clients_money)

print('\nСЛЕДУЮЩИЙЙЙ!!!')
