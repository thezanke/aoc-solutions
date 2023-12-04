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
        log = "✅"
    except AssertionError as e:
        log = f"❌ %s" % e

    print(f"{label}: {log} (~{execution_time:.3f}s)")
