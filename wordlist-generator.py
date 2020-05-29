import sys

file_rd = open(sys.argv[1],"r+")
list_of_words = file_rd.readlines()

num = int(sys.argv[2])
combined_words = []

if num <= 2:
	for i in range(0, len(list_of_words)):
		for j in range(0, len(list_of_words)):
			combined_words.append(list_of_words[i].strip()+list_of_words[j].strip())
elif num == 3:
	for i in range(0, len(list_of_words)):
		for j in range(0, len(list_of_words)):
			for k in range(0, len(list_of_words)):
				combined_words.append(list_of_words[i].strip()+list_of_words[j].strip()+list_of_words[k].strip())
elif num == 4:
	for i in range(0, len(list_of_words)):
		for j in range(0, len(list_of_words)):
			for k in range(0, len(list_of_words)):
				for l in range(0, len(list_of_words)):
					combined_words.append(list_of_words[i].strip()+list_of_words[j].strip()+list_of_words[k].strip()+list_of_words[l].strip())

with open("combined_words.txt", "w") as txt_file:
	for line in combined_words:
		txt_file.write("".join(line) + "\n")

    
