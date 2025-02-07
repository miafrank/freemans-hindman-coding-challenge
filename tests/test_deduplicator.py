import pytest

from exceptions.invalid_type_exception import InvalidTypeException


def create_expected_exception_message():
    return "Input cannot contain elements with different types"


@pytest.mark.parametrize("maybe_numeric_input, expected_exception_message", [
    (["a", {}, 1, "a", "b", "d"], create_expected_exception_message()),
    (["4", "b", 3, 2, 1.0, 1], create_expected_exception_message()),
    (["4", "b", 3, "?", [], 1], create_expected_exception_message()),
])
def test_input_with_different_types(deduplicator_instance,
                                             maybe_numeric_input,
                                             expected_exception_message):
    with pytest.raises(InvalidTypeException) as e:
        deduplicator_instance.validate_input_type(maybe_numeric_input)
        assert str(e.value) == expected_exception_message


@pytest.mark.parametrize("maybe_numeric_input, expected_result", [
    (["a", "b", "c", "a", "b", "d"], True),
    ([4, 4, 3, 2, 3, 1], True),
    ([{"c": "1"}, {"d": "1"}, {"a": "1"}], True),
    ([(1, 2), (10, 30), (11, 90)], True),
])
def test_input_with_same_type(deduplicator_instance,
                               maybe_numeric_input,
                               expected_result):
    assert deduplicator_instance.validate_input_type(maybe_numeric_input) == expected_result


@pytest.mark.parametrize("maybe_numeric_input, expected_result", [
    ([2, 3, 1, 9, 33, 17], True),
    (["a", "b", "c"], True),
    ([(1, 2), (10, 30), (11, 90)], True),
])
def test_input_with_distinct_elements(deduplicator_instance,
                                      maybe_numeric_input,
                                      expected_result):
    assert deduplicator_instance._has_only_unique_elements(maybe_numeric_input) == expected_result


@pytest.mark.parametrize("maybe_numeric_input, expected_result", [
    (["a", "b", "c", "a", "b", "d"], False),
    ([4, 4, 3, 2, 3, 1], False),
    ([(1, 2), (10, 30), (11, 90), (10, 30), (1, 2)], False),
])
def test_input_with_non_distinct_elements(deduplicator_instance,
                                          maybe_numeric_input,
                                          expected_result):
    assert deduplicator_instance._has_only_unique_elements(maybe_numeric_input) == expected_result
