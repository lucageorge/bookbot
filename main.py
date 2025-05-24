from stats import get_num_words 

def get_book_text(file_path):
    with open(file_path, "r") as file:
        return file.read()

def main():
    file_path = "books/frankenstein.txt" 
    book_text = get_book_text(file_path)
    print(f"{get_num_words(book_text)} words found in the document")

main()