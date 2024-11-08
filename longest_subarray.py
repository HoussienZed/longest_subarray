def longest_subarray(array):

    results_list = []
    for i in range(len(array)):

        # testing if the first element is one or zero
        """
        if array[0] == 0:
            count_zero = 1
            count_one = 0
        else:
            count_zero = 0
            count_one = 1
        """
        count_zero = 0
        count_one = 0
        # looping over subarrays to count zeros and ones
        for j in range(i, len(array)):

            if array[j] == 0:
                count_zero += 1
            else:
                count_one += 1

            if count_one == count_zero:  # appending the subarrays with equal ones and zero to results list
                results_list.append([i, j, j - i + 1])

    # extracting the subarray with maximum index 2 element which is the length of the subarray
    final_result = max(results_list, key=lambda i: i[2])

    return (print(f"The longest subarray starts at index {final_result[0]} and ends at {final_result[1]}"))


longest_subarray([0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0])
