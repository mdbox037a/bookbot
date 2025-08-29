def count_words(text):
    count = len(text.split())
    return count


def count_characters(text):
    character_string = text.lower()
    character_dictionary = {}

    for character in character_string:
        if character in character_dictionary:
            character_dictionary[character] += 1
        else:
            character_dictionary[character] = 1

    return character_dictionary
