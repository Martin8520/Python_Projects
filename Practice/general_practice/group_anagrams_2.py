from collections import defaultdict


def groupAnagrams(strs):
    anagrams = defaultdict(list)

    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)

    return list(anagrams.values())


print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))  # [["eat","tea","ate"],["tan","nat"],["bat"]]
print(groupAnagrams([""]))  # [[""]]
print(groupAnagrams(["a"]))  # [["a"]]
print(groupAnagrams(["listen", "silent", "enlist"]))  # [["listen","silent","enlist"]]
print(groupAnagrams(["abc", "bca", "cab", "cba", "bac"]))  # [["abc","bca","cab","cba","bac"]]
