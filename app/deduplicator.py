from collections import OrderedDict
from typing import List, Literal

from exceptions.invalid_type_exception import InvalidTypeException
from models.data_processor import DataProcessor


class Deduplicator(DataProcessor):
    def _has_only_unique_elements(self, deduplicate_elements: List[str]) -> bool:
        return sorted(deduplicate_elements) == sorted(list(set(deduplicate_elements)))

    def validate_input_type(self, deduplicate_elements: List[str]) -> Literal[True]:
        all_same_type = all(isinstance(el, type(deduplicate_elements[0])) for el in deduplicate_elements)
        if not all_same_type:
            raise InvalidTypeException("Input cannot contain elements with different types")
        return True

    def apply_filter(self, deduplicate_elements: List[str]) -> InvalidTypeException | list:
        self.validate_input_type(deduplicate_elements)

        if self._has_only_unique_elements(deduplicate_elements):
            return deduplicate_elements

        result = OrderedDict()
        for element in deduplicate_elements:
            result.setdefault(element, default=1)
            if element in result:
                result[element] += 1
        return list(result.keys())
