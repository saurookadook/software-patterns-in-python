import heapq


class MedianFinder:

    def __init__(self):
        self.heaps = ([], [])

    def add_num(self, num: int) -> None:
        """Process is as follows:

        1. When a new number arrives, we store the number in `large` heap (`MinHeap`).
        2. We maintain balance between the heaps by removing the smallest element from
            `large` and pushing it into `small` _(our simulated `MaxHeap`)_.
        3. If `large` has fewer elements than `small`, we balance it by pushing the
            largest element from `small` to `large`.
        """
        small, large = self.heaps
        heapq.heappush(small, -heapq.heappushpop(large, num))
        if len(large) < len(small):
            heapq.heappush(large, -heapq.heappop(small))

    def find_median(self):
        """Since `large` contains the larger elements, if `large` has more elements than
        `small`, the median is the smallest element in large.
        Otherwise, the median is the average of the smallest element in `large` and
        the largest in `small`.
        """
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        # We subtract `small[0]` from `large[0]` because `small` consists of negative values
        return float((large[0] - small[0]) / 2.0)
