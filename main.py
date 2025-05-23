from stats import word_count
from stats import count_char
from stats import sort_char_dict
import sys


def get_book_text(filePath):
    with open (filePath) as f:
        book = f.read()
    return book

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filePath = sys.argv[1]
    book = get_book_text(filePath)
    num_words = word_count(book)
    char_counts = count_char(book)
    sorted_chars = sort_char_dict(char_counts)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filePath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    #print(char_count)
    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")
    


main()