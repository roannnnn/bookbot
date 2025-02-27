<<<<<<< HEAD
import sys

from stats import get_book_text
from stats import get_num_words
from stats import make_char_dict
from stats import make_sorted_dict_list
from stats import format

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book")
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    char_dict = make_char_dict(book_text)
    sorted_dict_list = make_sorted_dict_list(char_dict)
    format(book_path, num_words, sorted_dict_list)

main()
=======
print("greetings boots")
>>>>>>> f32be32869a53805c45730d4dfee637144cdb04c
