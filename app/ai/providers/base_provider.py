from abc import ABC, abstractmethod


class BaseProvider(ABC):

    @abstractmethod
    def analyze_feed(self, content: str):
        pass