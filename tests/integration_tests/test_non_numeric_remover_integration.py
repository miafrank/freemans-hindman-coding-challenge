import pytest


@pytest.mark.parametrize("numeric_input, expected_result", [
    ("7-623", "7623"),
    ("..2965a", "2965"),
    ("cd-880-ab", "880"),
    ("934823", "934823"),
    ("aj*55", "55"),
    ("qw1e!as.912", "1912"),
])
def test_remove_non_numeric(non_numeric_remover_instance, numeric_input, expected_result):
    assert non_numeric_remover_instance.apply_filter(numeric_input) == expected_result
