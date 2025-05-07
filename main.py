from stats import word_count


def get_book_text(filePath):
    with open(filePath) as f:
        book = f.read()
    return book
        
def main():
    book = get_book_text('books/frankenstein.txt')
    num_words = word_count(book)
    print(f'{num_words} words found in the document')
   



main()



