"""Application functionals."""
import datetime
import random
from price import price_list

RECEIPT_WIDTH = 30

cart: dict[str, int | float] = {}


def get_cart_total_cost() -> float:
    """Get total cost of all products in the cart."""
    return sum(cart.values())


def get_change(clients_money: float) -> None:
    """Выдаем сдачу."""
    print(f'Ваша сдача {clients_money - get_cart_total_cost()}. Забирай и проваливай!')


def print_price_list():
    """Красиво распечатываем прайс лист."""
    print('*' * 30)
    print('ПРАЙС ЛИСТ'.center(30, '*'))
    print('*' * 30)

    for product_name, product_cost in price_list.items():
        price_line = (f'{product_name}: {product_cost} баксов за кило.')
        if product_cost >= 5:
            price_line += ' Да, дорого! Не нравится - не бери!'
        print(price_line)


def get_clients_money_amount() -> float:
    """
    Запрашиваем у покупателя, сколько у него денег.
    Если ответ нам не нравится - выгоняем его вон.
    """

    print('Деньги есть?!! Скока?')
    while True:
        try:
            clients_money = float(input())
            break
        except ValueError:
            print('Чего?!! Я про деньги спрашиваю. ДЕНЬГИ! ДЕ-НЮЖ-КИ!!!')
            continue

    if not clients_money:
        quit('Пшел вон отсюда, бомжара!')
    if clients_money < 0:
        quit(f'Вали давай отсюда! Ты нам и так уже должен {abs(clients_money)}!!!')

    return clients_money


def get_product_name() -> str:
    """Узнаем, какой товар хочет покупатель."""
    while True:
        product = input('Ну, чё брать то будешь?\n').capitalize()
        if product in price_list or not product:
            return product
        print(f'У нас нет никакого {product}!!! Ты что, слепой?!!!')


def get_weight() -> float:
    """Узнаем, сколько кг хочет покупатель."""
    while True:
        try:
            weight: float = abs(float(input('Сколько кило?\n')))
            return weight
        except ValueError:
            print('Я спросил сколько кило? ВЕС! А ты про что?!!!')


def start_byuing_process(clients_money):
    """
    1. Узнать, какой продукт нужен покупателю.
       Если пустая строка - завершаем покупки.
    2. Узнать сколько кг ему нужно.
    3. Выяснить, достаточно ли у покупателя денег
       чтобы добавить этот товар в корзину.
    4. Добавить товар в корзину.
    """

    def get_total_product_cost() -> float:
        """Узнаем общубю стоимость товара (цена за кг * вес)"""
        return price_list[product] * weight

    def enough_money_to_buy() -> bool:
        """
        Считаем, какая будет стоимость корзины после добавления нового
        товара. Если у покупателя достаточно денег чтобы это оплатить
        - возвращаем True. Если нет - False.
        """
        total_product_cost: float = get_total_product_cost()
        new_cart_sum = get_cart_total_cost() + total_product_cost
        if clients_money >= new_cart_sum:
            return True
        print(f'Тебе не хватает {new_cart_sum - clients_money}')
        return False

    def add_product_to_cart() -> None:
        """
        Добавляем товар в корзину, в зависимости от того,
        есть уже такой товар в корзине или нет.
        """
        if product in cart:
            cart[product] += get_total_product_cost()
        else:
            cart[product] = get_total_product_cost()

    while True:
        print_price_list()
        product = get_product_name()
        if not product:
            break
        weight = get_weight()
        if enough_money_to_buy():
            add_product_to_cart()
        print(f'Ты уже набрал тут на {get_cart_total_cost()}.')


def print_receipt():
    """Печатаем чек, перебирая корзину и выводя каждую строку."""
    receipt = '\n'

    def add_line(text: str) -> None:
        nonlocal receipt
        receipt += '|{}|'.format(text.center(RECEIPT_WIDTH))
        receipt += '\n'

    def add_price_line(product: str, cost: int | float) -> None:
        cost_str = str(cost)
        dots = '.' * (RECEIPT_WIDTH - len(product) - len(cost_str))
        price_line = f'{product}{dots}{cost_str}'
        add_line(price_line)

    add_line('')
    add_line('ЧП "Касперович"')
    add_line('Магазин "Гнилое яблоко"')
    add_line(f'Фискальный чек номер {random.randint(10_000, 99_999)}')
    add_line(datetime.datetime.now().strftime('%d.%m.%Y, %H:%M:%S'))
    add_line('')
    for product, cost in cart.items():
        add_price_line(product, cost)
    add_line('')
    add_price_line('Сумма', get_cart_total_cost())
    add_line('Приходите к нам еще!')
    add_line('')
    receipt += '^' * (RECEIPT_WIDTH + 2)
    with open('cash register tape', 'a') as f:
        f.writelines(receipt)
