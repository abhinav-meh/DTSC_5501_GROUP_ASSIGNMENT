def checkConflictsLinked(linked, return_list):
    import time
    # array is ArrayListEventStore to be searched for conflicts
    # return list is 1 to print a list of conflicts, 0 to skip printing (for large data sets)
    start_time = time.time() # start execution time

    # set variables to collect data
    checked = [] 
    conflicts = []
    conflict_id = []

    # zero counters
    con_instance = 0
    conflict_total = 0

    chk_point = linked.head
    while chk_point:
        
        #print(f"check point = {chk_point}")
        # Event parameters to check for conflicts
        chk_sked = chk_point.event.getTimestamp() # timestamp
        chk_loc = chk_point.event.getLocation() # location
        #print(f"chk_sked = {chk_sked}")
        #print(f"chk_loc = {chk_loc}")

        chk_combo = chk_loc + '_' + str(chk_sked) # date / time / location combined

        # check if date / time / location combination has been checked for conflicts already
        # if so, skip to next combination
        if(chk_combo in checked):
            #print(f"{chk_combo} already checked")
            chk_point = chk_point.next
            continue
        # if date / time / location combination has not been checked for conflicts, continue
        else:
            checked.append(chk_combo) # note combination being checked 
            #print(f"checking {chk_combo}")

        conflict_count = 0 # zero conflict count        

        # comparison starts with next event after event being checked
        query = chk_point.next
        

        while query:
            #print(f"query = {query}")

            # if match of timestamp and location
            #print(f"Timestamp compare: {query.event.getTimestamp()} vs {chk_sked}")
            #print(f"Location compare: {query.event.getLocation()} vx {chk_loc}")
            if(query.event.getTimestamp() == chk_sked and query.event.getLocation() == chk_loc):
                conflict_count +=1
                # if first conflict instance, note both event ids
                if(conflict_count == 1):
                    conflict_id.append(chk_point.event.getId())
                    conflict_id.append(query.event.getId())
                # if subsequent conflict instance, note only new event id
                else:
                    conflict_id.append(query.event.getId())
                #print(f"conflict identified - count {conflict_count}")
                #print(f"query = {query}")
                              
            query = query.next
        # if reach the end of the search and conflicts have been identified
        # document conflict counts and details
        if(conflict_count > 0):
            conflicts.append([chk_combo, conflict_count])
            con_instance += 1
            conflict_total += conflict_count
        
        chk_point = chk_point.next
        #print(f"new check point = {chk_point}")
        
    end_time = time.time() # stop execution time
    conflict_chk_time = end_time - start_time # calculate run time

    print(f"{conflict_total} conflicts identified for {con_instance} time / loc combinations")

    #print(f"Conflict List: {conflicts}")

    print(f"Conflict checking time: {conflict_chk_time} s")
    if(return_list == 1):
        return conflict_total, con_instance, conflict_chk_time, conflict_id
    else:
        return conflict_total, con_instance, conflict_chk_time      
