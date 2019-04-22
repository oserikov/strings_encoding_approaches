from abc import ABC, abstractmethod


class StringsCoder(ABC):

    @abstractmethod
    def encode(self, string_to_encode) -> str:
        pass

    @abstractmethod
    def decode(self, string_to_decode) -> str:
        pass
