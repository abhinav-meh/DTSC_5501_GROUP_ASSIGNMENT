from ArrayListEventStore import ArrayListEventStore
from Event_Random import Event_Random

def test_event_random_array(x):
    EventList = ArrayListEventStore(x)
    for i in range(x):           
        eventi = Event_Random(i+1)#, f"Event {i}", date, time_start, location)
        if(x<15):print(f"Event generated {eventi}")
        EventList.insert_event(eventi)
        
    return EventList    
