def word_count(book_text):
    words = book_text.split()
    count = len(words)
    return count



def character_count(book_text):
    total_characters = {}
    for characters in book_text:
        character = characters.lower()
        if character in total_characters:
            total_characters[character] = total_characters[character] + 1
        else:
            total_characters[character] = 1
        
    return total_characters



def sort_characters(total_characters):
    dict_list =[]
    for key, value in total_characters.items():
        if key.isalpha():
            dict_list.append({"char": key, "num": value})
    
    dict_list.sort(key=lambda item: item["num"], reverse=True)

    return dict_list 