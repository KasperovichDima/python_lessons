"""Application price list."""


# price_list: dict[str, float] = dict(
#     Капуста=0.98,
#     Кабачки=1.75,
#     Картошка=0.50,
#     Помидоры=1.25,
#     Манго=6.84,
#     Апельсины=3.45,
#     Бананы=1.30,
#     Черешня=7.50,
# )


def get_price_list() -> dict[str, float]:
    """Read data from file and return price list."""
    price_list: dict[str, float] = {}
    with open('price_file', 'r') as f:
        lines = f.readlines()
        for line in lines:
            line_data = line.split('=')
            product = line_data[0]
            cost = float(line_data[1])
            price_list[product] = cost
    return price_list


price_list = get_price_list()
