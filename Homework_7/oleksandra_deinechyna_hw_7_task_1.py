def square_parameters(size_of_the_side):
    perimeter = size_of_the_side*4
    diagonal = (2*(size_of_the_side**2))**(1/2)
    square_area = size_of_the_side**2
    return print((perimeter, diagonal, square_area))
square_parameters(10)

'''
написать функцию которая в качестве аргумента принимает размер стороны квадрата, а возвращает кортеж в котором лежат три значения:

    периметр квадрата
    диагональ квадрата
    площадь квадрата
'''
