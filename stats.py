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

def sort_on(char_count):
    return char_count["num"]

def finalReport(char_count):
    report = []
    for char, num in char_count.items():
        report.append({"char":char, "num": num})
    report.sort(reverse=True, key=sort_on)
    return report


