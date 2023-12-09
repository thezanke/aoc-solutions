from typing import Any, Callable
import timeit


def expectation(
    label: str,
    expected: Any,
    func: Callable[..., Any],
    *args: Any,
    **kwargs: Any,
) -> None:
    start_time = timeit.default_timer()
    value = func(*args, **kwargs)
    end_time = timeit.default_timer()
    execution_time = end_time - start_time

    try:
        assert value == expected, "expected %r, got %r" % (expected, value)
        log = "✅"
    except AssertionError as e:
        log = f"❌ %s" % e

    print(f"{label}: {log} (~{execution_time:.4f}s)")


def chunk_list(input_list: list[Any], chunk_size: int):
    return [
        input_list[i : i + chunk_size] for i in range(0, len(input_list), chunk_size)
    ]


def deduplicate(input_list: list[Any]):
    return list(set(input_list))
