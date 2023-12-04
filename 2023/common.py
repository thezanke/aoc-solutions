from typing import Any


def test(label: str, value: Any, expected: Any):
    assert value == expected, f"{label}: Expected {expected}, got {value}"
    print(f"{label}: OK")
