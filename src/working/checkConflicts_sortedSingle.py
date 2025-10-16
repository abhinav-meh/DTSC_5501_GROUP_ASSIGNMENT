import time
import random
import datetime

from src.event import Event
from src.ArrayListEventStore import ArrayListEventStore

def checkConflicts_sortedSingle(date, time, location, array, return_list):
    # submit details (date, time, location) for a single event to check for 
    # conflicts in array. 
    #return_list indicates if list of conflicts will be returned (1) or not (0)
    start_time = time.time() # start execution time
    # parse event date and time into pieces to make timestamp
    year, month, day = int(split(date,'-'))
    hr, mi = int(split(time,':'))

    # build timestamp for event to check
    chk_sked = str(datetime.datetime(year,month,day,hr,mi))
    chk_loc = location

    # parameters for binary search of timestamp
    min_ind = 0
    max_ind = array.len()-1

    runs = max_ind - min_ind + 1

    chk_pt = (max_ind - min_ind)//2

    start_chk = -1

    size = array.len()

    # set variables to collect data and zero counters
    conflicts = []
    conflict_id = []
    con_instance = 0
    conflict_total = 0
    conflict_count = 0

    # stepping through array to find index where event timestamp matches
    for i in range(runs):
    if(array.getTimestamp()[chk_pt] == chk_sked):
        # once event timestamp matches, step backwards to find first instance
        while array.getTimestamp()[chk_pt] == chk_sked:
            #print(chk_pt)
            chk_pt -=1
            
        start_chk = chk_pt+1 # array index to start comparison from
        print(f"searching array from: {start_chk}")
        break
    else:
        if(array.getTimestamp()[chk_pt] < chk_sked):
            min_ind = chk_pt + 1
            chk_pt = (max_ind - min_ind)//2
        else:
            max_ind = chk_pt -1
            chk_pt = (max_ind - min_ind)//2
    # if event timestamp is not found, no conflict exists
    if(start_chk == -1):
        print(f"No conflict identified")
    # check from 
    else:
        for k in range(start_chk,size):
            # once all instances of the timestamp have been checked for location,
            # no need to continue checking 
            if(array.getTimestamp()[k] != chk_sked):
                k = size
            # if conflict identified, record details
            elif(array.getTimestamp()[k] == chk_sked and array.getLocation()[k] == chk_loc):
                conflict_count +=1
                #if(conflict_count == 1):
                conflict_id.append(array.getId()[k])
                #print(f"conflict identified - count {conflict_count}")

        if(k == (size-1)) and conflict_count > 0: #k == event_id[-2]
            conflicts.append([chk_combo, conflict_count])
            con_instance += 1
            conflict_total += conflict_count
    
    end_time = time.time()
    conflict_chk_time = end_time - start_time
    
    print(f"{conflict_total} conflicts identified")
    print(conflict_id)

    if(return_list == 1):
        return conflict_total, con_instance, conflict_chk_time, conflict_id
    else:
        return conflict_total, con_instance, conflict_chk_time     
