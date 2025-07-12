import sys

from stats import word_count

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

with open(sys.argv[1], "r") as file:
    text = file.read()

total_words = word_count(text)

print(f"Found {total_words} total words")



from stats import character_count

total_character_count = character_count(text)


# print(total_character_count)



from stats import sort_characters

arranged_list = sort_characters(total_character_count)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}...")
print("----------- Word Count ----------")
print(f"Found {total_words} total words")
print("--------- Character Count -------")
for item in arranged_list:
    print(f"{item['char']}: {item['num']}")
print("============= END ===============")