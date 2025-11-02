import pytest
from faker import Faker

from ..heap_sort import heap_sort, heap_sort_in_place


# fake = Faker()


@pytest.mark.parametrize(
    "test_data",
    [
        ([]),
        ([Faker().unique.random_int(min=1, max=10) for _ in range(10)]),
        ([Faker().unique.random_int(min=1, max=2000) for _ in range(1000)]),
    ],
)
def test_heap_sort(test_data):
    sorted_data = sorted(test_data)

    sorted_result = heap_sort(test_data)

    assert sorted_result == sorted_data
    assert sorted_result is not test_data


@pytest.mark.parametrize(
    "test_data",
    [
        ([]),
        ([Faker().unique.random_int(min=1, max=10) for _ in range(10)]),
        ([Faker().unique.random_int(min=1, max=2000) for _ in range(1000)]),
    ],
)
def test_heap_sort_in_place(test_data):
    sorted_data = sorted(test_data)

    sorted_result = heap_sort_in_place(test_data)

    assert sorted_result == sorted_data
    assert sorted_result is not test_data
