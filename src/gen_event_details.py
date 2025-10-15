def gen_event_details():
    import datetime
    import random
    
    # Parameters for random generation of dates, times, and locations
    year = [2026]
    day = [31,28,31,30,31,30,31,31,30,31,30,31]
    hour = range(1,24)
    minute = [0]
    loc = ["Bldg 1", "Bldg 2", "Bldg 6", "Conf Rm 13", "Conf Rm 42", "Parking Lot 3"]

    # Generate date
    y = random.choice(year)
    
    mon = random.randint(1,12)
    if(mon<10):
        m = '0'+str(mon) 
    else: m = str(mon)
         
    D = day[mon-1]
    dy = random.randint(1,D)
    if(dy<10):
        d = '0'+str(dy) 
    else: d = str(dy)

    # Generate time
    h = random.randint(1,23)
    if(h<10): 
        hh = '0' + str(h) 
    else: hh = str(h)
        
    mi = 0
    mm = '00' 
    
    # Date 
    date = str(y)+'-'+ m +'-'+ d
    
    # Start time
    time_start =  hh + ':' + mm

    # Location
    location = random.choice(loc)

    # Generate datetime & timestamp
    dt = datetime.datetime(y,mon,dy,h,mi)
    timestamp = dt.timestamp()

    return date, time_start, timestamp, location
