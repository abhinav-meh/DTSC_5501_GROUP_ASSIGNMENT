from conflictCheck import checkConflicts
from genEventTestData import test_set_gen

# Known Repeat Testing Array
time_stamp0 = [1794216600.0, 1794216600.0, 1822746600.0, 1790785800.0, 1800075600.0, 1794216600.0,1770130800.0, 1822746600.0, 1822746600.0]
event_id0 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
location0 = ['Conf Rm 42', 'Conf Rm 42', 'Bldg 1', 'Conf Rm 42', 'Bldg 2', 'Conf Rm 42','Conf Rm 42','Bldg 1','Bldg 1',]

conflict_count_tot0, con_instances0, conflict_chk_time0, conflict_id_list0 = checkConflicts(event_id0, time_stamp0, location0)

print("Conflict Check Results: Event Set with Known Conflicts")
print(conflict_count_tot0)
print(con_instances0)
print(conflict_chk_time0)
print(conflict_id_list0)

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
    
    event_id, time_stamp, location = test_set_gen(z)

    conflict_count_tot[m], con_instances[m], conflict_chk_time[m] = checkConflicts(event_id, time_stamp, location,0)
    #, conflict_id_list[m]

    #C[m], results[m], con_id_list[m] = checkConflicts(event_id, time_stamp, location,1)

print("Conflict Check Results: Multiple Event Sets Randomly Generated"
print(f"Total conflicts identifed: {conflict_count_tot})")
print(f"Conflict instances: {con_instances}")
print(f"Time to check conflicts: {conflict_chk_time}")
#print(f"Event IDs with conflict: {conflict_id_list}")

import matplotlib.pyplot as plt

plt.plot(test_inc, conflict_chk_time, marker='o', linestyle='-', color='blue', label='?')
plt.xlabel("Events Checked")
plt.ylabel("Time (s)")
plt.title("Time to Execute Conflict Checking")
plt.grid(True)
plt.show()
