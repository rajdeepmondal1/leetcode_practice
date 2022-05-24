# 347. Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

def topKFrequent(nums, k):
    """
    :param nums: Inputs a list of integer numbers
    :param k: Inputs an integer.
    :return: k most frequent elements.
    """

    # Take a dictionary to store the numbers and their corresponding counts
    numbers = {}

    # Initialize an empty array(buckets) for every numbers in nums
    frequency = [[] for _ in range(len(nums) + 1)]

    # Count the number of occurrences of each number from nums
    for n in nums:
        numbers[n] = 1 + numbers.get(n, 0)

    # Append the number to the corresponding frequency of occurrences
    for number, counts in numbers.items():
        frequency[counts].append(number)

    result = []

    # Traversing the frequency list in reverse order
    for i in range(len(frequency) - 1, 0, -1):
        # Return top K results
        for n in frequency[i]:
            result.append(n)
            if len(result) == k:
                return result


print(topKFrequent([1, 1, 1, 2, 2, 3], 2))
print(topKFrequent([2], 1))
