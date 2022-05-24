# 49 - Group Anagrams - https://leetcode.com/problems/group-anagrams/

from collections import defaultdict


def groupAnagrams(strs):
    """
    :param strs:
    :return:
    """
    result = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for letter in s:
            count[ord(letter) - ord('a')] += 1
        result[tuple(count)].append(s)
    return result.values()


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
print(groupAnagrams([""]))
print(groupAnagrams(["a"]))
