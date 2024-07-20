# Given an array of N integers where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are m students, the task is to distribute chocolate packets such that: 

# Each student gets one packet.
# The difference between the number of chocolates in the packet with maximum chocolates and the packet with minimum chocolates given to the students is minimum.

def findMinDiff(arr, m):
    n = len(arr)

    if (n == 0 or m == 0):
        return 0

    arr.sort()

    if (n < m):
        return -1
    
    min_diff = arr[n-1] - arr[0]

    for i in range(n - m + 1):
        min_diff = min(min_diff, arr[i + m - 1] - arr[i])

    return min_diff