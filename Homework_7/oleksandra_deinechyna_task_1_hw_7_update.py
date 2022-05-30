"""
написать функцию которая в качестве аргумента принимает размер стороны квадрата, а возвращает кортеж в котором лежат три значения:
    периметр квадрата
    диагональ квадрата
    площадь квадрата
"""

def square_parameters(size_of_the_side):
    perimeter = size_of_the_side * 4
    diagonal = (2 * (size_of_the_side ** 2)) ** (1 / 2)
    square_area = size_of_the_side ** 2
    return f"{perimeter=}, {diagonal=}, {square_area=}"


print(square_parameters(10))


