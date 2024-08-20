from abc import ABC, abstractmethod

class Context(ABC):
    @abstractmethod
    def transition_to(self, state: 'State'):
        pass