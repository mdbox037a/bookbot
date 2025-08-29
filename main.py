from stats import count_words


def main():
    file_path = "books/frankenstein.txt"
    text = get_book_text(file_path)
    count = count_words(text)

    # print(text)
    print(f"{count} words found in the document")
    return 0


def get_book_text(file_path):
    with open(file_path) as path:
        file_contents = path.read()
    return file_contents


main()
