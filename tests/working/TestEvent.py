def test_event(x):
    EventList = []*x
    for i in range(x):           
        eventi = Event_Random(i+1)#, f"Event {i}", date, time_start, location)
        print(f"Event generated {eventi}")
        EventList.append(eventi)
        #print(event)
        #EventList[i] = event
    #print(EventList)
    return EventList  

A = test_event(10)

for y in range(10):
    
    print(f"Check data for index {y} \n ID: {A[y].getId()}, Title: {A[y].getTitle()}, Date: {A[y].getDate()}, Time: {A[y].getTime()}, Timestamp:{A[y].getTimestamp()}, Location:{A[y].getLocation()}")

