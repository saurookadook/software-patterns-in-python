import heapq


def heap_sort(iterable):
    """Heap sort is a comparison-based sorting algorithm that uses a binary heap data
    structure to sort elements. It works by first building a max heap from the input
    data, and then repeatedly extracting the maximum element from the heap and
    rebuilding the heap until all elements are sorted.

    - **Time Complexity**: _**O(n log n)**_ in all cases _(best, average, worst)_
    - **Space Complexity**: _**O(n)**_ - Requires copy of `n` _(maybe this isn't correct?)_

    Args:
        iterable: An `iterable` collection of comparable elements _(e.g., `list`, `tuple`)_.

    Returns:
        A new `list` containing the sorted elements.
    """
    h = []
    for value in iterable:
        heapq.heappush(h, value)
    return [heapq.heappop(h) for _ in range(len(h))]


def heap_sort_in_place(iterable):
    """Heap sort is a comparison-based sorting algorithm that uses a binary heap data
    structure to sort elements. It works by first building a max heap from the input
    data, and then repeatedly extracting the maximum element from the heap and
    rebuilding the heap until all elements are sorted.

    - **Time Complexity**: _**O(n log n)**_ - in all cases _(best, average, worst)_
    - **Space Complexity**: _**O(1)**_ - in-place sorting algorithm by removing elements from
            the original iterable and pushing them into a new iterable.

    Args:
        iterable: An `iterable` collection of comparable elements _(e.g., `list`, `tuple`)_.

    Returns:
        A new `list` containing the sorted elements.
    """
    heapq.heapify(iterable)
    return [heapq.heappop(iterable) for _ in range(len(iterable))]
