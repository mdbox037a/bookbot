from stats import count_words, count_characters, dictionary_sort


def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    word_count = count_words(text)
    character_dictionary = count_characters(text)
    sorted_character_count = dictionary_sort(character_dictionary)

    # output section
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")

    for dict in sorted_character_count:
        if dict["char"].isalpha():
            print(f"{dict['char']}: {dict['num']}")

    print("============= END ===============")

    return 0


def get_book_text(file_path):
    with open(file_path) as path:
        file_contents = path.read()
    return file_contents


main()
