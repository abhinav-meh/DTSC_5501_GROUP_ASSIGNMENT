from test_event_fixed_linked import test_event_fixed_linked
from test_event_random_linked import test_event_random_linked
from checkConflictsLinked import checkConflictsLinked

# generate list of known events
test_known_10 = test_event_fixed_linked(10)

# execute conflict checks for known events and report results
print("Linked List Conflict Check Results: Event Set with Known Conflicts")
conflict_total0, con_instances0, conflict_chk_time0, conflict_id_list0 = checkConflictsLinked(test_known_10, 1)
print(f"\nTotal conflicts identified: {conflict_total0}")
print(f"Number of date/time/location combinations with conflicts: {con_instances0}")
print(f"Time to run conflict checks: {conflict_chk_time0} s")
print(f"Event IDs of events with conflicts: {conflict_id_list0}\n")

for i in range(len(conflict_id_list0)):
    print(test_known_10.search_by_id(conflict_id_list0[i]))

# generate list of random events
test_random_10 = test_event_random_linked(10)

# execute conflict checks for set of random events and report results
print("Linked List Conflict Check Results: Random Event Set with 10 Events")
conflict_total1, con_instances1, conflict_chk_time1, conflict_id_list1 = checkConflictsLinked(test_random_10, 1)
print(f"\nTotal conflicts identified: {conflict_total1}")
print(f"Number of date/time/location combinations with conflicts: {con_instances1}")
print(f"Time to run conflict checks: {conflict_chk_time1} s")
print(f"Event IDs of events with conflicts: {conflict_id_list1}")

for i in range(len(conflict_id_list1)):
    print(test_random_10.search_by_id(conflict_id_list1[i]))

# generate larger list of random events
# execute conflict checks and report results
print("Linked List Conflict Check Results: Random Event Set with 500 Events")
test_random_500 = test_event_random_linked(500)
conflict_total2, con_instances2, conflict_chk_time2, conflict_id_list2 = checkConflictsLinked(test_random_500, 1)
print(f"\nTotal conflicts identified: {conflict_total2}")
print(f"Number of date/time/location combinations with conflicts: {con_instances2}")
print(f"Time to run conflict checks: {conflict_chk_time2} s")
print(f"Event IDs of events with conflicts: {conflict_id_list2}\n")

for i in range(len(conflict_id_list2)):
    print(test_random_500.search_by_id(conflict_id_list2[i]))


# Generate test arrays of variable sizes
test_inc = (50,500,1000,5000,10000,25000,50000)
ind = 0

n = len(test_inc)

conflict_count_tot = [0] * n
con_instances = [0] * n
conflict_chk_time = [0] * n
conflict_id_list = [0] * n

for m in range(n):
    z = test_inc[m]
    print(f"checking {z} events")
    #print(m)

    test_set = test_event_random_linked(z)
    
    conflict_count_tot[m], con_instances[m], conflict_chk_time[m] = checkConflictsLinked(test_set, 0)
    

print("Linked List Conflict Check Results: Multiple Event Sets Randomly Generated")
print(f"Total conflicts identifed: {conflict_count_tot})")
print(f"Conflict instances: {con_instances}")
print(f"Time to check conflicts: {conflict_chk_time}")


import matplotlib.pyplot as plt

plt.plot(test_inc, conflict_chk_time, marker='o', linestyle='-', color='blue', label='?')
plt.xlabel("Events Checked")
plt.ylabel("Time (s)")
plt.title("Time to Execute Conflict Checking For Linked List")
plt.grid(True)
plt.show()
