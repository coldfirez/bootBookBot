def word_count(book):
    num_words = len(book.split())
    return num_words

def count_char(book):
    char_counts = {}
    lower_char = book.lower()
    for char in lower_char:
        if char.isalpha():
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    return char_counts
    
def sort_on(char_counts):
    return char_counts["num"]

def sort_char_dict(char_counts):
    sorted_list = []

    for char, count in char_counts.items():
        if char.isalpha():
            sorted_list.append({"char": char, "num": count})
    
    sorted_list.sort(reverse = True, key= sort_on)
    return sorted_list