def replace_words(dictionary, sentence):
    dictionary.sort(key=len)

    words = sentence.split()

    def find_root(word):
        for root in dictionary:
            if word.startswith(root):
                return root
        return word

    replaced_words = [find_root(word) for word in words]

    return ' '.join(replaced_words)


dictionary = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
print(replace_words(dictionary, sentence))

dictionary = ["a", "b", "c"]
sentence = "aadsfasf absbs bbab cadsfafs"
print(replace_words(dictionary, sentence))
