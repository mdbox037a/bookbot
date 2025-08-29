from stats import count_words, count_characters


def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    word_count = count_words(text)
    character_count = count_characters(text)

    # print(text)
    print(f"{word_count} words found in the document")
    print(character_count)

    return 0


def get_book_text(file_path):
    with open(file_path) as path:
        file_contents = path.read()
    return file_contents


main()
