import math


def sum_numbers(a: int, b: int):
    return a + b


def example_function(a: int, b: int, c: int):
    if c == 0:
        return 0
    return (a * b) / c


def compute_area_of_a_circle(radius: float):
    return math.pow(radius, 2) * math.pi


def compute_area_of_a_triangle(base: float, height: float):
    return (base * height) / 2
