from dataclasses import dataclass

from faker import Faker

fake = Faker()


def _convert_post_code_to_name(post_code_digits: str) -> str:
    """Преобразует последовательность цифр почтового индекса в соответствующее имя.

    Args:
        post_code_digits (str): Последовательность цифр почтового индекса.

    Returns:
        str: Соответствующее имя.
    """
    post_code_numbers_list = [int(post_code_digits[x:x + 2]) for x in range(0, 10, 2)]

    # в соответствии с ascii таблицей символ "а" код "97"
    # i % 26 - остаток от деления код символа алфавита: a=0, b=1 ... a=26, b=27 ...
    ascii_code_list = [i % 26 + 97 for i in post_code_numbers_list]
    chars_list = [chr(i) for i in ascii_code_list]
    name = ''.join(chars_list).capitalize()

    return name


@dataclass
class Customer:
    """ Представляет собой клиента.

    Attributes:
        post_code (str): Почтовый индекс клиента.
        first_name (str): Преобразованное имя клиента.
        last_name (str): Фамилия клиента.
    """
    post_code: str = fake.numerify('##########')
    first_name: str = _convert_post_code_to_name(post_code)
    last_name: str = fake.last_name()
