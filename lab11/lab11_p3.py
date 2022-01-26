# File WordCount.py

def getFile():
    """
    Returns the file name and associated file object for reading the
    file  as tuple of the form (file_name, input_file).
    """
    input_file_opened = False
    while not input_file_opened:
        try:
            file_name = input('Enter input file name (with extension): ')
            input_file = open(file_name, 'r')
            input_file_opened = True
        except OSError:
            print('Unable to open input file, please reenter')
    return (file_name, input_file)


def countWords(input_file, search_word):
    """
    Returns the number of occurrences
    of search_word in the provided input_file object.
    """
    # set file pointer to beginning
    input_file.seek(0)
    num_occurrences = 0
    word_delimiters = (' ', ',', ';', ':', '.', '\n',
                       '"', "'", '(', ')')

    search_word_len = len(search_word)
    for line in input_file:
        line = line.lower()  # convert to lower case characters.
        end_of_line = False
        begin_of_line = True  # the begin of line counts as a word_delimiter
        while not end_of_line:
           try:
                found_search_word = False
                index = line.index(search_word)  # throws ValueError if not found
                if index == 0:
                    # Only valid case for 'index == 0' is at begin of line.
                    # In the middle of a line, line[index-1] must be a delimiter. If not,
                    # the word lacks a LEFT delimiter and we're in the middle of a
                    # word, for example at the second 'foo' in 'foofoo' when counting
                    # 'foo'. Thus, index==0 is not possible in the middle of a line.
                    if begin_of_line and line[search_word_len] in word_delimiters:
                        found_search_word = True
                elif index > 0:
                    # All matching cases in middle of line must have 'index > 0',
                    # because line[index - 1] must be a delimiter! (So index=0 is
                    # invalid, because the LEFT delimiter is missing.)
                    if line[index - 1] in word_delimiters and \
                            line[index + search_word_len] in word_delimiters:
                        found_search_word = True
                if found_search_word:
                    num_occurrences = num_occurrences + 1
                begin_of_line = False  # we moved past the begin of line
                line = line[index + search_word_len:]

           except ValueError:
                end_of_line = True
    return num_occurrences

#---
# main


# get file to count words
file_name, input_file = getFile()


word_delimiters = (' ', ',', ';', ':', '.', '\n', '"', "'", '(', ')')

# make all words in file into list
# init
list_words_in_file = []
list_result = []
# replace all delimiters into '/' and split strings by '/'
# then remove

for line in input_file:
    for delim in word_delimiters:
        while delim in line:
            line = line.replace(delim, '/')
    list_words_in_line = line.split('/')
    while '' in list_words_in_line:
        list_words_in_line.remove('')
    for i in list_words_in_line:
        if i.lower() not in list_words_in_file:
            list_words_in_file.append(i.lower())

# open file
input_file = open(file_name, 'r')

# count words and make result list
for word in list_words_in_file:

    num_occurrences = countWords(input_file, word)
    list_result.append([word, num_occurrences])


# naming .wc file
output_file_name = file_name[:-3]+'wc'

# output results
output_file = open(output_file_name, 'w')
# sort words in alphabet order
list_result.sort()
for i in list_result:
    output_file.write(i[0] + ': ' + str(i[1])+'\n')

# close files
output_file.close()
input_file.close()












