import pytest

from numigi_tests import redirect_exception


@pytest.mark.parametrize('source, target', [
    (ZeroDivisionError, ValueError),
    (ArithmeticError, IndexError),
    (NameError, AttributeError)
])
def test_redirect_exception_decorator(source, target):
    @redirect_exception(source, target)
    def func():
        raise source

    with pytest.raises(target):
        func()
