import time
import random
import datetime

from src.event import Event
from src.ArrayListEventStore import ArrayListEventStore

def checkConflicts_sortedSingle(date, time, location, array, return_list):
    start_time = time.time()
    year, month, day = int(split(date,'-'))
    hr, mi = int(split(time,':'))

    chk_sked = str(datetime.datetime(year,month,day,hr,mi))
    chk_loc = location

    min_ind = 0
    max_ind = array.len()-1

    runs = max_ind - min_ind + 1

    chk_pt = (max_ind - min_ind)//2

    start_chk = -1

    size = array.len()

    conflicts = []
    conflict_id = []
    con_instance = 0
    conflict_total = 0
    conflict_count = 0

    for i in range(runs):
    if(array.getTimestamp()[chk_pt] == chk_sked):
        while array.getTimestamp()[chk_pt] == chk_sked:
            #print(chk_pt)
            chk_pt -=1
            
        start_chk = chk_pt+1
        print(f"searching array from: {start_chk}")
        break
    else:
        if(array.getTimestamp()[chk_pt] < chk_sked):
            min_ind = chk_pt + 1
            chk_pt = (max_ind - min_ind)//2
        else:
            max_ind = chk_pt -1
            chk_pt = (max_ind - min_ind)//2

    if(start_chk == -1):
        print(f"No conflict identified")
    else:
        for k in range(start_chk,size):#event_id[-1]):
            if(array.getTimestamp()[k] == chk_sked and array.getLocation()[k] == chk_loc):
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
