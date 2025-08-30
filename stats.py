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


def dictionary_sort(character_count_dict):
    dictionaries_list = []

    for entry in character_count_dict:
        sub_dictionary = {}

        character_name = entry
        character_count = character_count_dict[entry]
        sub_dictionary["char"] = character_name
        sub_dictionary["num"] = character_count

        dictionaries_list.append(sub_dictionary)

    dictionaries_list.sort(reverse=True, key=sort_on)

    return dictionaries_list


def sort_on(items):
    return items["num"]
