def checkConflicts(event_id, time_stamp, location, return_list):
    start_time = time.time()

    checked = []
    conflicts = []
    conflict_id = []

    con_instance = 0
    conflict_total = 0
    
    for j in range(event_id[-1]):
        
        chk_sked = time_stamp[j]
        chk_loc = location[j]
        
        chk_combo = chk_loc + '_' + str(chk_sked)

        if(chk_combo in checked):
            #print(f"{chk_combo} already checked")
            continue
        else:
            checked.append(chk_combo)
            #print(f"checking {chk_combo}")

            conflict_count = 0
            
            for k in range(j+1,event_id[-1]):
                if(time_stamp[k] == chk_sked and location[k] == chk_loc):
                    conflict_count +=1
                    if(conflict_count == 1):
                        conflict_id.append(j+1)
                        conflict_id.append(k+1)
                    else:
                        conflict_id.append(k+1)
                    #print(f"conflict identified - count {conflict_count}")

            if(k == event_id[-2]) and conflict_count > 0:
                conflicts.append([chk_combo, conflict_count])
                con_instance += 1
                conflict_total += conflict_count
    end_time = time.time()
    conflict_chk_time = end_time - start_time

    print(f"{conflict_total} conflicts identified for {con_instance} time / loc combinations")

    print(f"Conflict checking time: {conflict_chk_time} s")
    
    if(return_list == 1):
        return conflict_total, con_instance, conflict_chk_time, conflict_id
    else:
        return conflict_total, con_instance, conflict_chk_time
