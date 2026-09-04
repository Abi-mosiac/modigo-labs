def find_longest_word(words):
    longest = words[0]
    # TODO: loop through `words` and update `longest` whenever
    # a strictly longer word is found
    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest