import re
import os

file_to_load = os.path.join("../raw_data", "paragraph_2.txt")
file_to_output = os.path.join("../analysis", "paragraph_2_analysis.txt")

with open(file_to_load) as paragraph_data:
	paragraph = paragraph_data.read()

	# get word count
	word_split = paragraph.split(" ")
	word_count = len(word_split)

	# get sentence count
	sentence_split = re.split("(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s", paragraph)
	sentence_count = len(sentence_split)

	# average letter count per word
	average_letters_per_word = round((len(paragraph)/word_count), 2)

	# average words per sentence
	average_words_per_sentence = round((word_count/sentence_count), 2)
	
	paragraph_output = (
		f"{paragraph}"
		f"\n--------------------------"
		f"\nParagraph Analysis"
		f"\n--------------------------"
		f"\nTotal word count: {word_count}"
		f"\nApproximate sentence count: {sentence_count}"
		f"\nApproximate letters per word: {average_letters_per_word}"
		f"\nApproximate words per sentence: {average_words_per_sentence}\n"
	)

	print(paragraph_output, end="")

	with open(file_to_output, "w") as txt_file:
		txt_file.write(paragraph_output)