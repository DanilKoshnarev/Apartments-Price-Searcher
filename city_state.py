from interfaces.state import State

class CityState(State):
    def __init__(self, street_service):
        self.street_service = street_service

    def handle(self, context, user_input: str):
        context.data["city"] = user_input
        streets = self.street_service.get_streets_by_city(user_input)
        print(f"Средняя цена квартир в городе {user_input}: ...")
        print(f"Доступные улицы в {user_input}: {', '.join(streets)}")

    def next_state(self):
        return "StreetState"