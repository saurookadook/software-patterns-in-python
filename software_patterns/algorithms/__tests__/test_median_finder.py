import pytest


from ..median_finder import MedianFinder


@pytest.fixture
def median_finder():
    return MedianFinder()
