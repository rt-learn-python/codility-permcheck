import pytest
from solution import solution


@pytest.mark.parametrize(('input', 'expected'), [
    # Happy path
    ([4, 1, 3, 2], 1),
    ([4, 1, 3], 0),
    ([1], 1),
    ([1, 1], 0),
    ([2], 0),
    ([x for x in range(1, 100_001)], 1),
    # Negative-Positive transitions.
    ])
def test_solution(input, expected):
    assert solution(input) == expected
