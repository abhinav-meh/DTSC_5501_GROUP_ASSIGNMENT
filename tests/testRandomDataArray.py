from test_event_random_array import test_event_random_array
from checkConflictsArray import checkConflictsArray

def testRandomDataArray(event_count,print_conflicts):
    test_random = test_event_random_array(event_count)

    print(f"Array List Conflict Check Results: Random Event Set with {event_count} Events")
    if(print_conflicts == 0):
        conflict_total1, con_instances1, conflict_chk_time1 = checkConflictsArray(test_random, print_conflicts)
    elif(print_conflicts == 1):
        conflict_total1, con_instances1, conflict_chk_time1, conflict_id_list1 = checkConflictsArray(test_random, print_conflicts)
        
    print(f"\nTotal conflicts identified: {conflict_total1}")
    print(f"Number of date/time/location combinations with conflicts: {con_instances1}")
    print(f"Time to run conflict checks: {conflict_chk_time1} s")
    if(print_conflicts ==1):
        print(f"Event IDs of events with conflicts: {conflict_id_list1}")
        
        for i in range(len(conflict_id_list1)):
            print(test_random.search_by_id(conflict_id_list1[i]))
            
        return conflict_total1, con_instances1, conflict_chk_time1, conflict_id_list1
    else:
        return conflict_total1, con_instances1, conflict_chk_time1
