from super_math import example_function


def test_when_a_and_b_and_c_are_one_result_is_one():
    a = 1
    b = 1
    c = 1
    expected = 1

    actual = example_function(a, b, c)

    assert expected == actual


def test_when_c_is_zero_then_result_should_be_zero():
    a = 1
    b = 1
    c = 0
    expected = 0

    actual = example_function(a, b, c)

    assert expected == actual

