def fullJustify(words, maxWidth):
    result = []
    line = []
    line_length = 0

    for word in words:
        if line_length + len(word) + len(line) <= maxWidth:
            line.append(word)
            line_length += len(word)
        else:
            spaces_to_add = maxWidth - line_length
            if len(line) == 1:
                result.append(line[0] + ' ' * spaces_to_add)
            else:
                space_between_words = spaces_to_add // (len(line) - 1)
                extra_spaces = spaces_to_add % (len(line) - 1)
                line_str = ''
                for i in range(len(line) - 1):
                    line_str += line[i] + ' ' * space_between_words
                    if i < extra_spaces:
                        line_str += ' '
                line_str += line[-1]
                result.append(line_str)

            line = [word]
            line_length = len(word)

    last_line = ' '.join(line)
    last_line += ' ' * (maxWidth - len(last_line))
    result.append(last_line)

    return result


words1 = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth1 = 16
print(fullJustify(words1, maxWidth1))

words2 = ["What", "must", "be", "acknowledgment", "shall", "be"]
maxWidth2 = 16
print(fullJustify(words2, maxWidth2))

words3 = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.", "Art",
          "is", "everything", "else", "we", "do"]
maxWidth3 = 20
print(fullJustify(words3, maxWidth3))
