from abc import ABC, abstractmethod

class State(ABC):
    @abstractmethod
    def handle(self, context, user_input: str):
        pass

    @abstractmethod
    def next_state(self):
        pass