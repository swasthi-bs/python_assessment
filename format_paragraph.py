from typing import List
import math

def justify_index(paragraph: str, page_width:int):

    """
    Justify the array index by distributing spaces between words

    Parameters:
    paragraph (string): Array indexes returned in above function 
    page width (int): Page width provided by the user

    Returns: Justified array with proper spacing
    """

    no_of_words = paragraph.split(" ")
    justified_paragraph=""
    length_without_space = len(paragraph.replace(' ', ''))
    number_of_spaces = page_width - length_without_space
    length_of_word = len(no_of_words)
    if length_of_word > 1:
        spaces = (number_of_spaces/(length_of_word-1))
    else :
        spaces = number_of_spaces
    i = 0
    used_space = 0
    for element in no_of_words:
        i += 1
        if i > 1 :
            used_space += math.floor(spaces)
        if length_of_word > 1:
            if not spaces.is_integer() and i == (length_of_word-1):
                justified_paragraph += element + " " * abs(used_space-number_of_spaces)
            else:
                justified_paragraph += element + " " * math.floor(spaces)
        else:
            justified_paragraph += element + " " * spaces
    return justified_paragraph

def create_arrays(paragraph: str, page_width:int):

    """
    Spilt the input paragraph string into array indexes of size equal to page width

    Parameters:
    paragraph (string): Array indexes returned in above function 
    page width (int): Page width provided by the user

    Returns:
    Splits the paragraph string and returns array of string
    """

    array = []
    string_to_insert = paragraph.split(" ")
    index = ""
    for words in string_to_insert:
        if len(words)+ len(index) <= page_width:
            index += words+ " "
        else:
            new_index= index.rstrip(index[-1])
            array.append(new_index)
            index = words+ " "
    new_index= index.rstrip(index[-1])
    array.append(new_index)
    return array

if __name__ == "__main__":
    paragraph = str(input("Enter paragraph: "))
    page_width = int(input("Enter page width : "))
    array = create_arrays(paragraph, page_width)
    for i in range(len(array)):
        justified_string = justify_index(array[i].strip(),page_width)
        print(f' Array {[i]}  = "{ justified_string.strip() if len(justified_string) > page_width else justified_string }"')

