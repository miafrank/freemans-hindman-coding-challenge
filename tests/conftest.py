import pytest

from app.deduplicator import Deduplicator
from app.non_numeric_remover import NonNumericRemover
from app.specialty_id_mapper import SpecialtyIDMapper


@pytest.fixture
def non_numeric_remover_instance():
    return NonNumericRemover()

@pytest.fixture
def deduplicator_instance():
    return Deduplicator()

@pytest.fixture
def specialty_id_mapper_instance(non_numeric_remover_instance, deduplicator_instance):
    return SpecialtyIDMapper(non_numeric_remover_instance, deduplicator_instance)
