from collections import deque


def word_ladder_length(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0

    queue = deque([(beginWord, 1)])
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    while queue:
        current_word, current_length = queue.popleft()

        if current_word == endWord:
            return current_length

        for i in range(len(current_word)):
            for char in alphabet:
                next_word = current_word[:i] + char + current_word[i + 1:]
                if next_word in wordSet:
                    wordSet.remove(next_word)
                    queue.append((next_word, current_length + 1))

    return 0


beginWord1 = "hit"
endWord1 = "cog"
wordList1 = ["hot", "dot", "dog", "lot", "log", "cog"]
print(word_ladder_length(beginWord1, endWord1, wordList1))  # 5

beginWord2 = "hit"
endWord2 = "cog"
wordList2 = ["hot", "dot", "dog", "lot", "log"]
print(word_ladder_length(beginWord2, endWord2, wordList2))  # 0
