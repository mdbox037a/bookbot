from stats import count_words, count_characters, dictionary_sort
import sys


def main():
    # input and help
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
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
