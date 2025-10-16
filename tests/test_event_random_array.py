from ArrayListEventStore import ArrayListEventStore
from Event_Random import Event_Random

def test_event_random_array(event_count):
    EventList = ArrayListEventStore(event_count)
    for i in range(event_count):           
        eventi = Event_Random(i+1)#, f"Event {i}", date, time_start, location)
        if(event_count<15):print(f"Event generated {eventi}")
        EventList.insert_event(eventi)
        
    return EventList    
