def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    wordcount = count_words(text)
    charcount = count_chars(text)
    print_report(book_path, wordcount, charcount)

def count_words(book):
    book_string = str(book)
    book_string = book_string.split()
    return len(book_string)

def count_chars(book):
    book_string = str(book)
    book_char = {}
    for x in book_string:
        if x.isalpha():
            book_lower = x.lower()
            if book_lower in book_char:
                book_char[book_lower] += 1
            else:
                book_char[book_lower] = 1
    return book_char

def get_book_text(path):
    with open(path) as f:
        return f.read()

def order_characters(sub_char):
    temp_dict = {}
    for items in range(len(sub_char)):
        temp_char = None
        temp_value = 0
        for x in sub_char:
            if sub_char[x] > temp_value:
                if x not in temp_dict:
                    temp_char = x
                    temp_value = sub_char[x]
        temp_dict[temp_char] = temp_value
    return temp_dict

def print_report(sub_path, sub_words, sub_chars):
    temp_chars = order_characters(sub_chars)
    print(f"\n--- Begin report of {sub_path} ---")
    print(f"{sub_words} were found in the document.\n")
    for x in temp_chars:
        print(f"The '{x}' character was found {temp_chars[x]} times.")
    print("--- End report ---")

main()