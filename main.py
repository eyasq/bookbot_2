from stats import count_words, counter,report
import sys

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
path = sys.argv[1]

def get_book_text(path):
    with open(path) as f:
        contents = f.read()
    return contents


def main():
    text = get_book_text(path)
    count = count_words(text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print( f"{count} words found in the document")
    print("--------- Character Count -------")
    # print(counter(text))
    letters_dict = counter(text)
    list_of_dics = (report(letters_dict))
    for entry in list_of_dics:
        if entry['char'].isalpha():
            print(f"{entry['char']}: {entry['count']}")
    print("============= END ===============")
main()