from day2 import __main__ as day2
from day3 import __main__ as day3
from day4 import __main__ as day4


def run():
    [day.run() for day in [day2, day3, day4]]


if __name__ == "__main__":
    run()
