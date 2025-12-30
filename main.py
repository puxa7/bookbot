from stats import words_counter
from stats import characters_counter
from stats import sortownica
import sys

def get_book_text(file_path):

    with open(file_path) as f:
        file_contents = ""
        file_contents = f.read()

    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)


    #book_string = get_book_text("./books/frankenstein.txt")
    book_string = get_book_text(sys.argv[1])
    

    num_words = words_counter(book_string)
    characters_dict = characters_counter(book_string)
    posortowana_lista = sortownica(characters_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in posortowana_lista:
        if i["char"].isalpha():
            print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

main()