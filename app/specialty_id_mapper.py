from typing import Literal
from app.deduplicator import Deduplicator
from app.non_numeric_remover import NonNumericRemover


no_matches = "No Matches Found"


class SpecialtyIDMapper:
    def __init__(self, non_numeric_remover: NonNumericRemover, deduplicator: Deduplicator):
        self.non_numeric_remover = non_numeric_remover
        self.deduplicator = deduplicator

    def _find_match_by_id(self, specialty_ids_deduplicated, specialty_names_by_id) -> list:
        result = [specialty_mapper[1]
                  for specialty_id in specialty_ids_deduplicated
                  for specialty_mapper in specialty_names_by_id
                  if specialty_id == specialty_mapper[0]]
        return result

    def get_specialty_names(self, specialty_ids, specialty_names_by_id) -> list | Literal['No Matches Found']:
        filtered_specialty_ids = list(map(self.non_numeric_remover.apply_filter, specialty_ids))
        filtered_specialty_ids_deduplicated = list(map(int, self.deduplicator.apply_filter(filtered_specialty_ids)))

        matches = self._find_match_by_id(filtered_specialty_ids_deduplicated, specialty_names_by_id)

        return no_matches if not matches else matches
