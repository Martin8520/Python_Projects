from collections import Counter


def frequencySort(s):
    frequency = Counter(s)

    sorted_chars = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    result = []
    for char, freq in sorted_chars:
        result.append(char * freq)

    return ''.join(result)


print(frequencySort("tree"))  # "eetr"
print(frequencySort("cccaaa"))  # "cccaaa"
print(frequencySort("Aabb"))  # "bbAa"
