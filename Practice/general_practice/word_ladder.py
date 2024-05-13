from collections import deque


def findLadders(beginWord, endWord, wordList):
    wordSet = set(wordList)

    if endWord not in wordSet:
        return []

    wordSet.add(beginWord)

    graph = {}
    for word in wordSet:
        graph[word] = []
        for i in range(len(word)):
            for j in range(26):
                new_word = word[:i] + chr(ord('a') + j) + word[i + 1:]
                if new_word in wordSet and new_word != word:
                    graph[word].append(new_word)

    queue = deque([(beginWord, [beginWord])])

    visited = set()

    sequences = []

    while queue:
        word, path = queue.popleft()

        if word == endWord:
            sequences.append(path)
            continue

        visited.add(word)

        for next_word in graph[word]:
            if next_word not in visited:
                queue.append((next_word, path + [next_word]))

    return sequences


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
print(findLadders(beginWord, endWord,
                  wordList))  # Output: [["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
