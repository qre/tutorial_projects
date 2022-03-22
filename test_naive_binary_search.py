import naive_binary_search
import pytest


@pytest.mark.naive
def test_naive_search():
    assert naive_binary_search.naive_search([1, 2, 3, 5, 10, 15], 10) == 4

@pytest.mark.naive
def test_naive_search_oob():
    assert naive_binary_search.naive_search([1, 100, 93, 40, 15, 18], 11) == -1

@pytest.mark.binary
def test_binary_search():
    assert naive_binary_search.binary_search([1, 24, 39, 42.5, 55, 70], 39, None, None) == 2

@pytest.mark.binary
def test_binary_search_low():
    assert naive_binary_search.binary_search([1, 3, 10, 25, 49, 78], 25, 1, 10) == 3

@pytest.mark.xfail
def test_binary_search_low_toolow():
    assert naive_binary_search.binary_search([1, 10, 20, 35, 58], 5, 10, None) == 1 #fails, as it should

@pytest.mark.binary
def test_binary_search_high():
    assert naive_binary_search.binary_search([2, 49, 50, 22, 60, 99], 60, 1, 9) == 4

@pytest.mark.xfail
def test_binary_search_high_toohigh():
    assert naive_binary_search.binary_search([1, 20, 39, 58], 50, None, 49) == 1 #fails, as it should
