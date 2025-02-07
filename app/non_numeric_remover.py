from typing import Any, List

from exceptions.invalid_type_exception import InvalidTypeException
from models.data_processor import DataProcessor


class NonNumericRemover(DataProcessor):
    def _identify_numeric_chars(self, maybe_numeric_input: str) -> List[str | bool]:
        return [_ if _.isdigit() else False for _ in maybe_numeric_input]

    def _contains_some_numeric_chars(self, maybe_numeric_input: str) -> bool:
        return any(self._identify_numeric_chars(maybe_numeric_input))

    def _contains_all_numeric_chars(self, maybe_numeric_input: str) -> bool:
        return all(self._identify_numeric_chars(maybe_numeric_input))

    def validate_input_type(self, maybe_numeric_input: str) -> bool:
        if not isinstance(maybe_numeric_input, str):
            raise InvalidTypeException(
                f"Input type: {type(maybe_numeric_input)} is not of type str")
        return True

    def apply_filter(self, maybe_numeric_input: str) -> InvalidTypeException | str:
        self.validate_input_type(maybe_numeric_input)

        if self._contains_all_numeric_chars(maybe_numeric_input):
            return maybe_numeric_input

        if self._contains_some_numeric_chars(maybe_numeric_input):
            filtered_chars = filter(str.isdigit, maybe_numeric_input)
            return ''.join(filtered_chars)

        raise InvalidTypeException('Input does not contain any ints')
