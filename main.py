def main():
    from stats import get_letter_report, get_book_word_count, get_letter_count
    import sys
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_to_file = sys.argv[1]
    text = get_book_text(path_to_file)

    word_count = get_book_word_count(text)
    letter_count = get_letter_count(text)
    char_list = get_letter_report(letter_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    
    for item in char_list:
        print(f"{item['char']}: {item['count']}")
    
    print("============= END ===============")

    
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

main()