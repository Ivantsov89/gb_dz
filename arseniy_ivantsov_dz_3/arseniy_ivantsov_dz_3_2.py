def thesaurus(*args) -> dict:
    dictionary = {}
    for name in args:
        key = name[0].capitalize()
        if key not in dictionary:
            dictionary[key] = []
        dictionary[key].append(name)
    return dictionary

    return dictionary


print(thesaurus("Иван", "Мария", "Петр", "Илья"))