import naive_binary_search
import pytest

@pytest.mark.naive
def test_naive_search():
    assert naive_binary_search.naive_search(20, 5) == 5

@pytest.mark.naive
def test_naive_search_oob():
    assert naive_binary_search.naive_search(10, 11) == None

@pytest.mark.binary
def test_binary_search():
    assert naive_binary_search.binary_search(100, 25, None, None) == 25

@pytest.mark.binary
def test_binary_search_low():
    assert naive_binary_search.binary_search(20, 5, 1, None) == 5

@pytest.mark.binary
def test_binary_search_low_toolow():
    assert naive_binary_search.binary_search(20, 5, 10, None) == 5

@pytest.mark.binary
def test_binary_search_high():
    assert naive_binary_search.binary_search(30, 5, None, 29) == 5

@pytest.mark.binary
def test_binary_search_high_toohigh():
    assert naive_binary_search.binary_search(200, 50, None, 49) == 5
