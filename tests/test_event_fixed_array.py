from ArrayListEventStore import ArrayListEventStore
from Event import Event

def test_event_fixed_array(event_count):
    import random
    EventList = ArrayListEventStore(event_count)
    for i in range(event_count): 
        if (i//2 !=0 and i < 4):
            eventi = Event(i+1, f"Event {i+1}", "2026-01-01", "10:00", "Conf Rm 42")
        else:
            s = random.randint(1,event_count)
            if(s//2 == 0 and s>5):
                eventi = Event(i+1, f"Event {i+1}", "2026-07-13", "15:00", "Bldg 2")
            elif(s == 5): 
                eventi = Event(i+1, f"Event {i+1}", "2026-04-19", "18:00", "Bldg 2")
            elif(s//3 ==0): 
                eventi = Event(i+1, f"Event {i+1}", "2026-12-06", "06:00", "Bldg 1")
            else:
                eventi = Event(i+1, f"Event {i+1}", "2026-12-06", "10:00", "Bldg 2")
        print(f"Event generated {eventi}")
        EventList.insert_event(eventi)
        
    return EventList    
