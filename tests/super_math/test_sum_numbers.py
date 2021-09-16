from super_math import \
    sum_numbers, \
    compute_area_of_a_circle, \
    compute_area_of_a_triangle


def test_when_a_and_b_are_grater_than_zero_result_is_consistent():
    # prepare
    a = 5
    b = 6
    expected = 11

    # Act
    actual = sum_numbers(a, b)

    # Assert
    assert expected == actual


def test_when_a_is_zero_result_is_equal_to_b():
    # prepare
    a = 0
    b = 6
    expected = b

    # Act
    actual = sum_numbers(a, b)

    # Assert
    assert expected == actual


def test_when_b_is_zero_result_is_equal_to_a():
    # prepare
    a = 5
    b = 0
    expected = a

    # Act
    actual = sum_numbers(a, b)

    # Assert
    assert expected == actual


def test_when_a_and_b_are_zero_result_is_zero():
    # prepare
    a = 0
    b = 0
    expected = 0

    # Act
    actual = sum_numbers(a, b)

    # Assert
    assert expected == actual


def test_when_a_is_negative_the_result_substracts_from_total():
    # prepare
    a = -5
    b = 6
    expected = 1

    # Act
    actual = sum_numbers(a, b)

    # Assert
    assert expected == actual
