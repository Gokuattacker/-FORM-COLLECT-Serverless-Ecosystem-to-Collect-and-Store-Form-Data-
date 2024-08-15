from abc import ABC, abstractmethod


class DataModel(ABC):

    @property
    @abstractmethod
    def data(self):
        pass

    def to_dict(self):
        payload = {}
        for key, value in self.data.items():
            if isinstance(value, DataModel):
                payload[key] = value.to_dict()
            elif value is not None:
                payload[key] = value
        return payload
        