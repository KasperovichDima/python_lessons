def print_price_list(price: dict[str, float]) -> None:
    """Print specified price list."""
    print('*' * 30)
    print('ПРАЙС ЛИСТ'.center(30, '*'))
    print('*' * 30)

    for product_name, product_cost in price.items():
        price_line = (f'{product_name}: {product_cost} баксов за кило.')
        if product_cost >= 5:
            price_line += ' Да, дорого! Не нравится - не бери!'
        print(price_line)
