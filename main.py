from stats import word_count
from stats import num_char
from stats import finalReport


def get_book_text(filePath):
    with open(filePath) as f:
        book = f.read()
    return book
        


def main():
    filePath = 'books/frankenstein.txt'
    book = get_book_text(filePath)
    num_words = word_count(book)
    char_count = num_char(book)
    report_final = finalReport(char_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filePath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    for item in report_final:
        if item["char"].isalpha():
            print(f'{item["char"]}: {item["num"]}')


    print("============= END ===============")

   



main()




