import time
import random
import datetime

def checkConflicts(array, return_list):
    # array is array/list to be searched for conflicts
    # return list is 1 to print a list of conflicts, 0 to skip printing (for large data sets)
    start_time = time.time()

    checked = [] 
    conflicts = []
    conflict_id = []

    con_instance = 0
    conflict_total = 0

    size = array.len()
    
    for j in range(size):
        #print(j)
        chk_sked = array.getTime()[j] #first 
        chk_loc = array.getLocation()[j]
        
        chk_combo = chk_loc + '_' + str(chk_sked)

        if(chk_combo in checked):
            #print(f"{chk_combo} already checked")
            continue
        else:
            checked.append(chk_combo)
            #print(f"checking {chk_combo}")

            conflict_count = 0
            
            for k in range(j+1,size):#event_id[-1]):
                if(array.getTimestamp()[k] == chk_sked and array.getLocation()[k] == chk_loc):
                    conflict_count +=1
                    if(conflict_count == 1):
                        conflict_id.append(event_id[j])
                        conflict_id.append(event_id[k])
                    else:
                        conflict_id.append(event_id[k])
                    #print(f"conflict identified - count {conflict_count}")

            if(k == (size-1)) and conflict_count > 0: #k == event_id[-2]
                conflicts.append([chk_combo, conflict_count])
                con_instance += 1
                conflict_total += conflict_count
    end_time = time.time()
    conflict_chk_time = end_time - start_time

    print(f"{conflict_total} conflicts identified for {con_instance} time / loc combinations")

    #print(f"Conflict List: {conflicts}")

    print(f"Conflict checking time: {conflict_chk_time} s")
    if(return_list == 1):
        return conflict_total, con_instance, conflict_chk_time, conflict_id
    else:
        return conflict_total, con_instance, conflict_chk_time  
