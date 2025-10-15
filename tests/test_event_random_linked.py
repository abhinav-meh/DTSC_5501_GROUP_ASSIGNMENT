from LinkedListEventStore import LinkedListEventStore
from EventStore import EventStore
from Event_Random import Event_Random
from Node import Node


def test_event_random_linked(x):
    EventList = LinkedListEventStore()
    for i in range(x):           
        eventi = Event_Random(i+1)#, f"Event {i}", date, time_start, location)
        if(x<15):print(f"Event generated {eventi}")
        EventList.insert_event(eventi)
        
    return EventList    
