import sys

from stats import get_word_count
from stats import get_char_count
from stats import sort_char_dict

def get_book_text(filepath):
    with open(filepath, encoding='utf8') as f:
         file_contents = f.read()

    wordcount = get_word_count(file_contents)
    charcount = get_char_count(file_contents)

    sorteddict = sort_char_dict(charcount)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {wordcount} total words")
    print("--------- Character Count -------")
    for s in sorteddict:
        if s['char'].isalpha():
           print(f"{s['char']}: {s['num']}")    
    print("============= END ===============")
    #print(str(charcount))
    

def main():
    if len(sys.argv) < 2:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)
    else:
       get_book_text(sys.argv[1])

main()