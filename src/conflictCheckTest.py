# Known Repeat Testing Array
time_stamp0 = [1794216600.0, 1794216600.0, 1822746600.0, 1790785800.0, 1800075600.0, 1794216600.0,1770130800.0, 1822746600.0, 1822746600.0]
event_id0 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
location0 = ['Conf Rm 42', 'Conf Rm 42', 'Bldg 1', 'Conf Rm 42', 'Bldg 2', 'Conf Rm 42','Conf Rm 42','Bldg 1','Bldg 1',]

conflict_report, con_chk_time = checkConflicts(event_id0, time_stamp0, location0)

# Generate test arrays of variable sizes
test_inc = (50,500,5000,50000)

for z in test_inc:
    n = len(test_inc)

    #results = [] * n

    event_id, time_stamp, location = test_set_gen(z)

    C, results = checkConflicts(event_id, time_stamp, location)

print(results) 
