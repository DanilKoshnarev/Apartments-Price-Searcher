import json

class StreetService:
    def __init__(self, data_file):
        with open(data_file, 'r') as file:
            self.streets_data = json.load(file)

    def get_streets_by_city(self, city):
        return self.streets_data.get(city, [])

# Запуск микросервиса
if __name__ == "__main__":
    street_service = StreetService("data/ukraine_streets.json")

    city = "Kyiv"
    streets = street_service.get_streets_by_city(city)
    print(f"Streets in {city}: {streets}")