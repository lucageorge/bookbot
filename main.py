import sys
from stats import get_num_words, get_ascii_distribution, prepare_report_data 

def get_book_text(file_path):
    with open(file_path, "r") as file:
        return file.read()

def print_report(file_path, book_text):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")
    print("--------- Character Count -------")
    for d in prepare_report_data(get_ascii_distribution(book_text)):
        if d['char'].isalpha():
            print(f"{d['char']}: {d['num']}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    print_report(file_path, book_text)

main()
