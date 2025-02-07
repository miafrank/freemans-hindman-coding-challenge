from abc import ABC, abstractmethod


class DataProcessor(ABC):
    @abstractmethod
    def validate_input_type(self, data):
        pass

    @abstractmethod
    def apply_filter(self, data):
        pass
