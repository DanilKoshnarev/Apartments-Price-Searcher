from interfaces.state import State

class StreetState(State):
    def handle(self, context, user_input: str):
        context.data["street"] = user_input
        print(f"Вы выбрали улицу {user_input}")

    def next_state(self):
        return "HouseNumberState"  # Здесь можно добавить следующее состояние (например, номер дома)