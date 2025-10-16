import random
from Event import Event

class EventGen:
    @staticmethod
    def generate_random_event(event_id: int) -> Event:
        locations = ['Conf Rm 42', 'Conf Rm 42', 'Bldg 1', 'Conf Rm 42', 'Bldg 2', 'Conf Rm 42', 'Conf Rm 42', 'Bldg 1', 'Bldg 1']
        dates = range(1, 29)
        time = f"{random.randint(0, 23):02}:{random.randint(0, 0):02}"
        location = random.choice(locations)
        date = f"2025-10-{random.choice(dates):02}"

        return Event(event_id, f"Event {event_id}", date, time, location)

    @staticmethod
    def generate_n_random_events(n: int, event_store) -> None:

        for event_id in range(1, n + 1):
            random_event = EventGen.generate_random_event(event_id)
            event_store.insert_event(random_event)