def groupAnagrams(strs):
    anagrams = {}

    for s in strs:
        sorted_s = ''.join(sorted(s))
        if sorted_s not in anagrams:
            anagrams[sorted_s] = [s]
        else:
            anagrams[sorted_s].append(s)

    return list(anagrams.values())


strs1 = ["eat", "tea", "tan", "ate", "nat", "bat", "tab"]
print(groupAnagrams(strs1))

strs2 = [""]
print(groupAnagrams(strs2))

strs3 = ["a"]
print(groupAnagrams(strs3))
