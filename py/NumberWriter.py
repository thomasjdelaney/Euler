from typing import Union, List


def split_number(number: int, split_length: int = 3) -> List[str]:
    """For splitting a number up into substrings of length split length. The first element of the list returned
    will be of length len(str(number)) % split_length.
    Args:
        number: the number to split
        split_length: the length of the splits
    Returns:
        a list of strings"""
    number_str = str(number)
    extra = len(number_str) % split_length
    if extra:
        starting = number_str[:extra]
        rest = number_str[extra:]
        split = [starting] + [rest[i:i + split_length] for i in range(0, len(rest), split_length)]
    else:
        split = [number_str[i:i + split_length] for i in range(0, len(number_str), split_length)]
    return split


class NumberWriter:
    """A class for writing numbers out in words."""
    num_to_str = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine",
        10: "ten",
        11: "eleven",
        12: "twelve",
        13: "thirteen",
        14: "fourteen",
        15: "fifteen",
        16: "sixteen",
        17: "seventeen",
        18: "eighteen",
        19: "nineteen",
        20: "twenty",
        30: "thirty",
        40: "forty",
        50: "fifty",
        60: "sixty",
        70: "seventy",
        80: "eighty",
        90: "ninety",
    }

    order_magnitude_str = {
        2: "thousand",
        3: "million",
        4: "billion",
        5: "trillion",
        6: "quadrillion",
        7: "quintillion",
        8: "sextillion",
        9: "septillion",
    }

    def __init__(self, n: int) -> None:
        """For initialising the object"""
        self.n = n
        self.written = ''
        self.set_written()

    def set_written(self) -> None:
        """For writing self.n in words."""
        if self.n in self.num_to_str:
            self.written = self.num_to_str[self.n]
        else:
            three_digit_split = split_number(self.n)
            for i, tds in enumerate(three_digit_split):
                self.written += f"{self.write_three_digit(number=tds)} "
                order_magnitude = len(three_digit_split) - i
                self.written += f"{self.order_magnitude_str.get(order_magnitude, '')} "
            self.written = self.written.strip()

    def write_three_digit(self, number: Union[str, int]) -> str:
        """For writing a three-digit number in words.
        Args:
            number: the number or a string of the number
        Returns:
            the number written in english"""
        if isinstance(number, int):
            number_str = str(number)
            number_int = number
        elif isinstance(number, str):
            number_str = number
            number_int = int(number_str)
        else:
            raise ValueError(f"Argument is the wrong type! {type(number)}")
        if len(number_str) > 3:
            raise ValueError(f"Number too long! {number_str}")
        mod_hundred = number_int % 100
        hundreds = number_str[0]
        if mod_hundred in self.num_to_str:
            num_in_words = self.num_to_str.get(mod_hundred)
        else:
            mod_ten = number_int % 10
            tens = (number_int - mod_ten) % 100
            num_in_words = f"{self.num_to_str.get(mod_ten, '')}"
            if tens:
                num_in_words = f"{self.num_to_str.get(tens, '')}-{num_in_words}"
        if len(number_str) > 2 and hundreds != "0":
            if num_in_words:
                num_in_words = f"{self.num_to_str.get(int(number_str[0]), '')} hundred and {num_in_words}"
            else:
                num_in_words = f"{self.num_to_str.get(int(number_str[0]), '')} hundred"
        return num_in_words
