# Задача:
# Каждый человек обладает именем, зарплатой, может быть застрахован или нет.
# У нас есть отдельно 6 имен, 6 зарплат, 6 страховок. Нужно их объединить
# и сделать команду из людей. То есть:
# (('Nika', 2700, True), ('Nastya', 3200, False), ...)

names: tuple[str, ...] = (
    'Bob',
    'John',
    'Charly',
    'Emma',
    'Nikole',
    'Antony'
)

salary_per_month: tuple[int, ...] = (
    4500,
    1500,
    0,
    12_000,
    6350,
    2600
)

has_ensurance: tuple[bool, ...] = (
    True,
    False,
    False,
    True,
    True,
    True
)

Person = tuple[str, int, bool]
Team = tuple[Person, ...]


# Wrong way to it
def get_persons_1() -> Team:
    result: list[Person] = []
    for ind in range(len(names)):
        p_name = names[ind]
        p_salary = salary_per_month[ind]
        p_ensurance = has_ensurance[ind]
        result.append((p_name, p_salary, p_ensurance))

    return tuple(result)


t1 = get_persons_1()
print(t1)


# Correct way to do it
def get_persons_2() -> Team:
    result = zip(names, salary_per_month, has_ensurance)  # Дает нам zip-объект
    return tuple(result)


t2 = get_persons_2()
print(t2)
