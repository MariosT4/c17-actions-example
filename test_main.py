"""Tests for main.py."""

from main import estimate_frog_count


def test_estimate_frog_count_returns_int():
    """Checks that the function returns an integer."""

    assert isinstance(estimate_frog_count(), int)
