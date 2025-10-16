from LinkedListEventStore import LinkedListEventStore
from EventStore import EventStore
from Event_Random import Event_Random
from Node import Node


def test_event_random_linked(event_count):
    EventList = LinkedListEventStore()
    for i in range(event_count):           
        eventi = Event_Random(i+1)#, f"Event {i}", date, time_start, location)
        if(event_count<15):print(f"Event generated {eventi}")
        EventList.insert_event(eventi)
        
    return EventList    
