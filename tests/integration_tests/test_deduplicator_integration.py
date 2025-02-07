import pytest


@pytest.mark.parametrize("maybe_numeric_input, expected_result", [
    (["a", "b", "c", "a", "b", "d"], ["a", "b", "c", "d"]),
    ([4, 4, 3, 2, 3, 1], [4, 3, 2, 1]),
    ([10, 4, 4, 33, 5, 2, 6, 1], [10, 4, 33, 5, 2, 6, 1]),
    ([12.1, 7.5, 12.1, 10.3, 7.5], [12.1, 7.5, 10.3]),
    ([True, False, True, True], [True, False]),
    ([False, False, False], [False]),
    ([True, True, True], [True]),
    ([False, True, False], [False, True]),
])
def test_remove_duplicates(deduplicator_instance, maybe_numeric_input, expected_result):
    assert deduplicator_instance.apply_filter(maybe_numeric_input) == expected_result
