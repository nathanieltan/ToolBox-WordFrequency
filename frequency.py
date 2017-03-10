""" Analyzes the word frequencies in a book downloaded from
Project Gutenberg """

import string


def get_word_list(file_name="pg1260.txt"):
    """ Reads the specified project Gutenberg book.  Header comments,
    punctuation, and whitespace are stripped away.  The function
    returns a list of the words used in the book as a list.
    All words are converted to lower case.
    """
    words = []
    f = open(file_name, 'r')
    lines = f.readlines()
    start_line = 0
    end_line = 0
    while lines[start_line].find('START OF THE PROJECT GUTENBERG EBOOK') == -1:
        start_line += 1
    while lines[end_line].find('***END OF THE PROJECT GUTENBERG EBOOK JANE EYRE***') == -1:
        end_line+=1
    lines = lines[start_line+1:end_line]
    trantab = str.maketrans('','',string.punctuation)
    for x in range(len(lines)):
        line = lines[x].strip().split()
        for a in range(len(line)):
            word = line[a].lower()
            words.append(word.translate(trantab))
    return words

def get_top_n_words(word_list, n):
    """ Takes a list of words as input and returns a list of the n most frequently
    occurring words ordered from most to least frequently occurring.

    word_list: a list of words (assumed to all be in lower case with no
    punctuation
    n: the number of words to return
    returns: a list of n most frequently occurring words ordered from most
    frequently to least frequentlyoccurring
    """
    frequency = {}
    result = []
    for x in range(len(word_list)):
        frequency[word_list[x]] = frequency.get(word_list[x],0)+1
    sortedFrequency = sorted(frequency, key=frequency.__getitem__, reverse = True)
    counter = 0
    for key in sortedFrequency:
        result.append(key)
        counter += 1
    return result[0:n]

if __name__ == "__main__":
    print("Running WordFrequency Toolbox")
    print(get_top_n_words(get_word_list(),100))
