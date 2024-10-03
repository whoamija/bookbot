def main():

	def get_book_text(path: str) -> str:
		with open(path) as f:
			return f.read()

	def get_word_count(book: str) -> int:
			book = book.split()
			return(len(book))	
	
	def get_characters_dict(book: str) -> dict:
		book = book.lower()
		char_count = {}
		for char in book:
				if char in char_count:
					char_count[char] += 1
				else:
					char_count[char] = 1
		return(char_count)

	def sort_on(dict):
		return dict["num"]

	def chars_dict_to_sorted_list(character_dict: dict) -> dict:
		sorted_list = []
		for element in character_dict:
			sorted_list.append({"char": element, "num": character_dict[element]})
		sorted_list.sort(reverse=True, key=sort_on)
		return sorted_list

	book_path = "./books/frankenstein.txt"
	book_contents = get_book_text(book_path)
	word_count = get_word_count(book_contents)
	character_dict = get_characters_dict(book_contents)
	character_sorted_list = chars_dict_to_sorted_list(character_dict)

	#print(book_contents)
	#print(word_count(book_contents))
	#print(character_dict)
	print(character_sorted_list)

	print(f"--- Begin report of {book_path} ---")
	print(f"{word_count} words found in the document")
	print()

	for item in character_sorted_list:
		if not item["char"].isalpha():
			continue
		print(f"The '{item['char']}' character was found {item['num']} times")

	print("--- End report ---")

main()