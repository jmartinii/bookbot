def get_book_word_count(text):
    return len(text.split())

def get_letter_count(text):
    letter_count = {}
    for char in text.lower():
        if char in letter_count:
            letter_count[char] += 1
        else:
            letter_count[char] = 1
    return letter_count 

def get_letter_report(letter_count):
    char_list = []
    for char, count in letter_count.items():
        if char.isalpha():
            char_list.append({"char": char, "count": count})
    char_list.sort(reverse=True, key=lambda x: x["count"])
    return char_list
    
        
    

