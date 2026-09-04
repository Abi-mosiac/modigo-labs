def total_word_count(sentences):
    count = 0

    for sentence in sentences:
        s = len(sentence.split())
        count += s

        
    return count