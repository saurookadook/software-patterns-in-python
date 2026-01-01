from typing import Any


def safe_get(callable) -> Any | None:
    """Example usage:

    ```python
    some_dict = dict(a="b", c="d")
    safe_get(lambda: some_dict["a"])  # returns `"b"`
    safe_get(lambda: some_dict["nope"])  # returns `None`
    ```

    Args:
        `callable`: A callable object to be safely executed.

    Returns:
        `Any | None`: If callable executes without error, returns its value. \
            Otherwise, returns `None`.
    """
    try:
        return callable()
    except (
        AttributeError,
        NameError,
        IndexError,
        KeyError,
    ):
        return None
