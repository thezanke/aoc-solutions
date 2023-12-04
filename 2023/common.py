from typing import Any, Callable
import timeit


def test(
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
        res_str = "✅"
    except AssertionError as e:
        res_str = f"❌ %s" % e

    print(f"{label}: {res_str} (~{execution_time:.3f}s)")
