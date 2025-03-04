#Problem:

#We have a list of dates in string format (e.g., "2023-05-15"), and we want to sort them in ascending order using the Insertion Sort algorithm instead of using built-in sorting methods.

#Solution:

#We will use the Insertion Sort algorithm to sort the list by converting each date string into a comparable datetime object.

#Python Code:

from datetime import datetime

def insertion_sort_dates(dates):
    """
    This function sorts a list of date strings (YYYY-MM-DD) in ascending order 
    using the Insertion Sort algorithm.
    """
    for i in range(1, len(dates)):  # Start from the second element
        key = dates[i]  # Current date to be inserted in the correct position
        j = i - 1

        # Convert date strings to datetime objects for comparison
        key_date = datetime.strptime(key, "%Y-%m-%d")

        while j >= 0 and datetime.strptime(dates[j], "%Y-%m-%d") > key_date:
            dates[j + 1] = dates[j]
            j -= 1

        dates[j + 1] = key  # Insert the date in its correct position

# Unsorted list of dates
dates_list = ["2023-05-15", "2021-12-01", "2022-07-30", "2020-03-25", "2023-01-10"]

# Print the list before sorting
print("Before sorting:", dates_list)

# Apply the insertion sort algorithm
insertion_sort_dates(dates_list)

# Print the list after sorting
print("After sorting:", dates_list)

#Expected Output:

#Before sorting: ['2023-05-15', '2021-12-01', '2022-07-30', '2020-03-25', '2023-01-10']
#After sorting: ['2020-03-25', '2021-12-01', '2022-07-30', '2023-01-10', '2023-05-15']

#The list is now sorted in ascending order based on the dates.