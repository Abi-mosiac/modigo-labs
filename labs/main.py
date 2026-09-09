def compare_hobbies(person1_hobbies, person2_hobbies):
    # TODO: use set operations to find shared, only_person1, and only_person2 hobbies
    dictionary = {}
    dictionary["shared"] = person1_hobbies.intersection(person2_hobbies)
    dictionary["only_person1"] = person1_hobbies - person2_hobbies
    dictionary["only_person2"] = person2_hobbies - person1_hobbies
    return dictionary