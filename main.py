def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)

 #Start of the report section
    print(f"---Bookbot report of '{book_path}' file---")   
    print(f"The document contains {num_words} words.")
    print()
    print("List of unique characters in the document:")
    for key, value in num_characters.items():
        print(f"The '{key}' character occurred {value} times.")
    print(f"---End of the Bookbot report---")   
#End of the report section

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_characters(text):
    characters = {}
    lowered_string = text.lower()
    for char in lowered_string:
        if ord(char) >= 97 and ord(char) <= 122:
            characters[char] = characters.get(char, 0) +1
    return characters

main()