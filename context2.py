from interfaces.context import Context
from interfaces.state import State

class BotContext(Context):
    def __init__(self, initial_state: State):
        self.current_state = initial_state
        self.data = {}

    def transition_to(self, state: State):
        self.current_state = state

    def process_input(self, user_input: str):
        self.current_state.handle(self, user_input)
        next_state_name = self.current_state.next_state()
        if next_state_name:
            new_state = globals()[next_state_name]()
            self.transition_to(new_state)
        else:
            print("Workflow complete.")