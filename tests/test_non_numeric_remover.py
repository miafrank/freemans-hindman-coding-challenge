import pytest
from exceptions.invalid_type_exception import InvalidTypeException


def create_expected_exception_message(input_type):
    return f"Input type: {type(input_type)} is not of type str"


@pytest.mark.parametrize("maybe_numeric_input, expected_exception_message", [
    ([], create_expected_exception_message([])),
    ({}, create_expected_exception_message({})),
    ((), create_expected_exception_message(())),
    (1, create_expected_exception_message(1)),
    (False, create_expected_exception_message(False)),
    (True, create_expected_exception_message(True)),
])
def test_contains_str_type_invalid_types(non_numeric_remover_instance, maybe_numeric_input, expected_exception_message):
    if expected_exception_message is not None:
        with pytest.raises(InvalidTypeException) as ex:
            non_numeric_remover_instance.validate_input_type(maybe_numeric_input)
        assert str(ex.value) == expected_exception_message
    else:
        assert non_numeric_remover_instance.validate_input_type(maybe_numeric_input)


@pytest.mark.parametrize("maybe_numeric_input, expected_result", [
    ('ajkdksfd', True),
    ('1290ajds', True),
    ('!!00xx&&', True),
])
def test_contains_str_type_valid_types(non_numeric_remover_instance, maybe_numeric_input, expected_result):
    assert non_numeric_remover_instance.validate_input_type(maybe_numeric_input) == expected_result


@pytest.mark.parametrize("maybe_numeric_input, expected_result", [
    ("934*823", True),
    ("143124.", True),
    ("abc1!", True),
    ("1xps", True),
])
def test_contains_some_numeric_chars(non_numeric_remover_instance, maybe_numeric_input, expected_result):
    assert non_numeric_remover_instance._contains_some_numeric_chars(maybe_numeric_input) == expected_result


@pytest.mark.parametrize("maybe_numeric_input, expected_result", [
    ("qowe.uqw", False),
    ("!!!aasd", False),
])
def test_does_not_contain_some_numeric_chars(non_numeric_remover_instance, maybe_numeric_input, expected_result):
    assert non_numeric_remover_instance._contains_some_numeric_chars(maybe_numeric_input) == expected_result


@pytest.mark.parametrize("numeric_input, expected_result", [
    ("880", True),
    ("934823", True),
])
def test_contains_all_numeric_chars(non_numeric_remover_instance, numeric_input, expected_result):
    assert non_numeric_remover_instance._contains_all_numeric_chars(numeric_input) == expected_result

