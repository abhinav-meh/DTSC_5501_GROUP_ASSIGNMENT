from testRandomDataArray import testRandomDataArray

def test_mult_cases_array(test_inc):
    ind = 0

    n = len(test_inc)

    conflict_count_tot = [0] * n
    con_instances = [0] * n
    conflict_chk_time = [0] * n
    conflict_id_list = [0] * n

    for m in range(n):
        z = test_inc[m]
        print(f"checking {z} events")
        #print(z)

        conflict_count_tot[m], con_instances[m], conflict_chk_time[m] = testRandomDataArray(z,0)

    import matplotlib.pyplot as plt

    plt.plot(test_inc, conflict_chk_time, marker='o', linestyle='-', color='blue', label='?')
    plt.xlabel("Events Checked")
    plt.ylabel("Time (s)")
    plt.title("Time to Execute Conflict Checking for Array List")
    plt.grid(True)
    plt.show()
