def word_count(book):
    num_words = book.split()
    return len(num_words)

def num_char(book):
    char_count = {}
    characters_lower = book.lower()
    for char in characters_lower:
        if char in char_count:
            char_count[char] +=1
        else:
            char_count[char] = 1
    return char_count
