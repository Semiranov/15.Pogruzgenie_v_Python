from fractions import Fraction


def add_and_multiply_fractions(fraction1, fraction2):
    # Преобразуем строки в объекты класса Fraction
    fraction1 = Fraction(fraction1)
    fraction2 = Fraction(fraction2)
    # Вычисляем сумму и произведение дробей
    sum_fraction = fraction1 + fraction2
    multiply_fraction = fraction1 * fraction2
    # Приводим результаты к строкам вида "a/b"
    sum_fraction_str = f"{sum_fraction.numerator}/{sum_fraction.denominator}"
    multiply_fraction_str = f"{multiply_fraction.numerator}/{multiply_fraction.denominator}"
    return sum_fraction_str, multiply_fraction_str


# Вводим две дроби с числителем и знаменателем
frac1 = '1/2'
frac2 = '1/3'
sum_fraction, multiply_fraction = add_and_multiply_fractions(frac1, frac2)
# Выводим результаты
print("Сумма дробей:", sum_fraction)
print("Произведение дробей:", multiply_fraction)
