def test_set_gen(n):
    # Set empty arrays 
    event_id = [0] * n
    date = ['NA'] * n
    time_start = ['NA'] * n
    location = ['NA'] * n
    time_stamp = ['NA'] * n
    
    # Parameters for random generation of dates, times, and locations
    year = [2026]
    day = [31,28,31,30,31,30,31,31,30,31,30,31]
    hour = range(1,24)
    minute = [0,30]
    loc = ["Bldg 1", "Bldg 2", "Bldg 6", "Conf Rm 13", "Conf Rm 42", "Parking Lot 3"]
    
    for j in range(n):
        # Set event ID
        event_id[j] = j+1
        
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
            
        mi = random.choice(minute)
        if(mi == 0): 
            mm = '00' 
        else: mm = '30'
        
        # Generate datetime
        dt = datetime.datetime(y,mon,dy,h,mi)
        
        # Date array
        date[j] = str(y)+'-'+ m +'-'+ d
        # Schedule Time array
        time_start[j] =  hh + ':' + mm
        # Location array
        location[j] = random.choice(loc)
        # Time Stamp array
        time_stamp[j] = dt.timestamp()
        
    return event_id, time_stamp, location
