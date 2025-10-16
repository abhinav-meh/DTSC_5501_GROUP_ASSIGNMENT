from test_event_fixed_array import test_event_fixed_array
from checkConflictsArray import checkConflictsArray

def testKnownDataArray(event_count):
    test_known = test_event_fixed_array(event_count)

    print("Array List Conflict Check Results: Event Set with Known Conflicts")
    conflict_total0, con_instances0, conflict_chk_time0, conflict_id_list0 = checkConflictsArray(test_known, 1)
    print(f"\nTotal conflicts identified: {conflict_total0}")
    print(f"Number of date/time/location combinations with conflicts: {con_instances0}")
    print(f"Time to run conflict checks: {conflict_chk_time0} s")
    print(f"Event IDs of events with conflicts: {conflict_id_list0}\n")

    for i in range(len(conflict_id_list0)):
        print(test_known.search_by_id(conflict_id_list0[i]))

    return conflict_total0, con_instances0, conflict_chk_time0, conflict_id_list0
