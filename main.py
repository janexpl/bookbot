from stats import get_num_words
from stats import get_num_letters
from stats import sorted_list
import sys


def get_book_text(file_path):
    file_content = ""
    with open(file_path) as file:
        file_content = file.read()
    return file_content


def print_raport(num_words, letters, file_path):
    header = f"""============ BOOKBOT ============\n
Analyzing book found at {file_path}\n
----------- Word Count ----------\n
Found {num_words} total words\n
--------- Character Count -------\n"""
    print(header)
    for letter in letters:
        if letter["char"].isalpha():
            print(f"{letter['char']}: {letter['num']}")
    print("============= END ===============")


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    num_words = get_num_words(book_text)
    letters = sorted_list(get_num_letters(book_text))
    print_raport(num_words, letters, file_path)


if __name__ == "__main__":
    main()
