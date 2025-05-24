from stats import get_num_words, get_ascii_distribution, prepare_report_data 

def get_book_text(file_path):
    with open(file_path, "r") as file:
        return file.read()

def main():
    file_path = "books/frankenstein.txt" 
    book_text = get_book_text(file_path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")
    print("--------- Character Count -------")
    for d in prepare_report_data(get_ascii_distribution(book_text)):
        if d['char'].isalpha():
            print(f"{d['char']}: {d['num']}")
    print("============= END ===============")


main()