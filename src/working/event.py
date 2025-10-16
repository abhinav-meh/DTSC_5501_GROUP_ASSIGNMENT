class Event():
    def __init__(self, id:int, title:str = None, date:str = "", time:str = "", location:str = ""):
        self.id = id
        self.title = str(id) if title is None else title
        self.date = date
        self.time = time
        self.location = location

    def getId(self):
        return self.id
    
    def getTitle(self):
        return self.title
    
    def getDate(self):
        return self.date
    
    def getTime(self):
        return self.time
    
    def getLocation(self):
        return self.location

    def setDate(self, date:str):
        self.date = date

    def setTime(self, time:str):
        self.time = time
    
    def setLocation(self, location:str):
        self.location = location
        
    def __str__(self):
        return f"Event(ID: {self.id}, Title: {self.title}, Date: {self.date}, Time: {self.time}, Location: {self.location})"
