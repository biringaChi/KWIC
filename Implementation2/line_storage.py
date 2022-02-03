'''
Author:
    Alexander J. Moulton
    Github: @moul-10
Usage:
    line_storage = LineStorage()
    line_storage.store_lines(List_of_strings_from_input)
    shifter.shift(line_storage.get_line(0))
    etc...
    '''
from typing import List

from linestorage_interface import LineStorageInterface
from word import Word


class LineStorage(LineStorageInterface):

    def __init__(self):
        super().__init__()
        self.__data = []
        self.__permutations = []

    def store_lines(self, lines: List[str]) -> None:
        for line in lines:
            # split string line into separate words
            list_of_string_words = line.split(' ')
            line_list_of_words = []
            for word in list_of_string_words:
                # add separate word strings into list of Word objects
                line_list_of_words.append(Word(word))
            # save list in memory
            self.__data.append(line_list_of_words)

    def get_line(self, idx: int) -> str:
        word_strings = []
        for word in self.__data[idx]:
            # make list of word strings
            word_strings.append(word.get_content())
        # return joined string words into 1 string with spaces
        return ' '.join(word_strings)

    def store_permutations(self, permutations: List[List[int]]):
        self.__permutations = permutations

    def get_permutations(self) -> List[str]:
        """Returns list of strings from indexes to start from"""
        permutations_list = []
        for starting_index_list in self.__permutations:
            # get indices from which to start from
            for starting_index in starting_index_list:
                # for each index in the list, piece together one string
                # from Word object contents and add to list
                permutation = []
                current_index = starting_index
                done = False
                line = self.__data.__getitem__(self.__permutations.index(starting_index_list))

                while not done:
                    # print("Current Index: ", current_index)
                    permutation.append(line.__getitem__(current_index).get_content())
                    current_index = (current_index + 1) % (len(line))

                    if current_index == starting_index:
                        done = True
                permutations_list.append(' '.join(permutation))

        return permutations_list






