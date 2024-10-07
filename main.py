def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    print(f"Number of unique characters: {num_characters}")

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
        characters[char] = characters.get(char, 0) +1
    return characters

main()