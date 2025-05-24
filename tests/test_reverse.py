import pytest

def reverse(string):
    """Переворачивает строку."""
    return string[::-1]

from txt import text
from reverse_txt import reversed_text

def test_reverse_long_text():
    """Тестирует функцию reverse() с длинным текстом."""
    reversed_text_from_func = reverse(text)
    assert reversed_text_from_func == reversed_text

