def get_book_text(file_path):
    with open(file_path) as path:
        file_contents = path.read()
    return file_contents


def main():
    file_path = "books/frankenstein.txt"
    print(f"{get_book_text(file_path)}")
    return 0


main()
