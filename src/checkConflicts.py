import time
import random
import datetime

from src.event import Event
from src.ArrayListEventStore import ArrayListEventStore

def checkConflicts(array, return_list):
    # array is array/list to be searched for conflicts
    # return list is 1 to print a list of conflicts, 0 to skip printing (for large data sets)
    start_time = time.time() # start execution time

    # set variables to collect data
    checked = [] 
    conflicts = []
    conflict_id = []

    # zero counters
    con_instance = 0
    conflict_total = 0

    size = array.len()
    
    for j in range(size):
        #print(j)
        # Event parameters to check for conflicts
        chk_sked = array.getTime()[j] # timestamp
        chk_loc = array.getLocation()[j] # location
        
        chk_combo = chk_loc + '_' + str(chk_sked) # date / time / location combined

        # check if date / time / location combination has been checked for conflicts already
        # if so, skip to next combination
        if(chk_combo in checked):
            #print(f"{chk_combo} already checked")
            continue
        # if date / time / location combination has not been checked for conflicts, continue
        else:
            checked.append(chk_combo) # note combination being checked 
            #print(f"checking {chk_combo}")

            conflict_count = 0 # zero conflict count

            # comparison starts with next event after event being checked
            for k in range(j+1,size):
                # if match of timestamp and location
                if(array.getTimestamp()[k] == chk_sked and array.getLocation()[k] == chk_loc):
                    conflict_count +=1
                    # if first conflict instance, note both event ids
                    if(conflict_count == 1):
                        conflict_id.append(event_id[j])
                        conflict_id.append(event_id[k])
                    # if subsequent conflict instance, note only new event id
                    else:
                        conflict_id.append(event_id[k])
                    #print(f"conflict identified - count {conflict_count}")
            # if reach the end of the search and conflicts have been identified
            # document conflict counts and details
            if(k == (size-1)) and conflict_count > 0: 
                conflicts.append([chk_combo, conflict_count])
                con_instance += 1
                conflict_total += conflict_count
    end_time = time.time() # stop execution time
    conflict_chk_time = end_time - start_time # calculate run time

    print(f"{conflict_total} conflicts identified for {con_instance} time / loc combinations")

    #print(f"Conflict List: {conflicts}")

    print(f"Conflict checking time: {conflict_chk_time} s")
    if(return_list == 1):
        return conflict_total, con_instance, conflict_chk_time, conflict_id
    else:
        return conflict_total, con_instance, conflict_chk_time      
