class Event_Random():
    def __init__(self, id:int):#, title:str = None, date:str = "", time:str = "", location:str = ""):
        
        self.date, self.time, self.timestamp, self.location = gen_event_details() #return date, time_start, timestamp, location
        
        self.id = id
        self.title = str(id) #if title is None else title
        #self.date = date
        #self.time = time
        #self.location = random.choice(loc)
        #$self.timestamp = 

    def getId(self):
        return self.id
    
    def getTitle(self):
        return self.title
    
    def getDate(self):
        return self.date
    
    def getTime(self):
        return self.time

    def getTimestamp(self):
        return self.timestamp
    
    def getLocation(self):
        return self.location

    def setDate(self, date:str):
        self.date = date

    def setTime(self, time:str):
        self.time = time
    
    def setLocation(self, location:str):
        self.location = location
        
    def __str__(self):
        return f"Event(ID: {self.id}, Title: {self.title}, Date: {self.date}, Time: {self.time}, Timestamp: {self.timestamp}, Location: {self.location})"

