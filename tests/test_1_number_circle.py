from numigi_tests import circle_of_numbers


def test_circle_of_numbers():
    assert 7 == circle_of_numbers(n=10, first_number=2)
    assert 2 == circle_of_numbers(n=10, first_number=7)
    assert 3 == circle_of_numbers(n=4, first_number=1)
    assert 0 == circle_of_numbers(n=6, first_number=3)
