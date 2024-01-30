 #This programme is written to print the letters and the words in given string in upper and lower cases altenatively
str = input("Please enter a string to be manipulated :   ")

#Print the given string with the letters in upper and lower cases alternatively
char_alt_str = ""

for index in range(1, len(str)+1):

    if index % 2 != 0:
        new_char = str[index - 1].upper()

    else:
        new_char = str[index - 1].lower()

    char_alt_str += new_char

print(char_alt_str)

#Print the given string with the words in lower and upper cases alternatively
str_list = str.split()
word_alt_str = []

for index in range(1, len(str_list) + 1):

    if index % 2 != 0:
        new_word = str_list[index - 1].lower()

    else:
        new_word = str_list[index - 1].upper()

    word_alt_str.append(new_word)

word_alt_str = " ".join(word_alt_str)
print(word_alt_str)
