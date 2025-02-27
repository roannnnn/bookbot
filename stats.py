def get_book_text(book_path):
    with open(book_path) as book:
         return book.read()

def get_num_words(book_text):
    word_list = book_text.split()
    num_words = 0
    for word in word_list:
        num_words += 1
    return num_words

def make_char_dict(book_text):
    lowercase_book_text = book_text.lower()
    char_dict = {}
    for char in lowercase_book_text:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict

def sort_on(dict_item):
    char = list(dict_item.keys())[0]
    return dict_item[char]

def make_sorted_dict_list(char_dict):
    dict_list = []
    for char, count in char_dict.items():
        single_pair_dict = {char: count}
        dict_list.append(single_pair_dict)
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

def format(book_path, num_words, sorted_dict_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for dict in sorted_dict_list:
        char = list(dict.keys())[0]
        if char.isalpha():
            count = dict[char]
            print(f"{char}: {count}")
    print("============= END ===============")
    