from services.street_service import StreetService
from states.city_state import CityState
from states.country_state import CountryState
from core.context import BotContext

def main():
    # Инициализация микросервиса улиц
    street_service = StreetService("data/ukraine_streets.json")

    # Инициализация начального состояния
    initial_state = CountryState()

    # Инициализация контекста с начальным состоянием
    context = BotContext(initial_state)

    # Взаимодействие с пользователем
    user_input = input("Введите страну: ")
    context.process_input(user_input)

    # Переход к следующему состоянию (город)
    user_input = input("Введите город: ")
    context.process_input(user_input)

    # Переход к следующему состоянию (улица)
    user_input = input("Введите улицу: ")
    context.process_input(user_input)

    # Пример последующего состояния (номер дома)
    user_input = input("Введите номер дома: ")
    context.process_input(user_input)

if __name__ == "__main__":
    main()