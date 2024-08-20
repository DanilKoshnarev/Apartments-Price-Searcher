from interfaces.state import State

class CountryState(State):
    def handle(self, context, user_input: str):
        context.data["country"] = user_input
        print(f"Средняя цена квартир в стране {user_input}: ...")

    def next_state(self):
        return "CityState"