def remove_duplicates(items):
    # TODO: use a loop to build a new list with duplicates removed, keeping first occurrences
    result = []
    for item in items:
        if item not in result:
            result.append(item)
    return result