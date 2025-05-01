"""Example Python."""

from random import randint


def estimate_frog_count():
    """Estimates the number of frogs."""

    return randint(0, 10)


if __name__ == "__main__":
    print(estimate_frog_count())
