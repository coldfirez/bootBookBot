def get_book_text(filePath):
    with open(filePath) as f:
        book = f.read()
    return book
        
def main():
    book = get_book_text('books/frankenstein.txt')
    print(book)

#main()



