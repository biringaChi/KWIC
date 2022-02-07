'''
Author:
    Alexander J. Moulton
    Github: @moul-10

Usage:
    circ_shift = CircularShifter()
    list_of_shifted_strings = circ_shift.shift("This is my input string")
'''

import numpy as np
from interface.circular_shifter_interface import CircularShifterInterface


class CircularShifter(CircularShifterInterface):

    # Only used to keep Object-Oriented, no attributes needed
    # This could be made static by removing class def

    def __init__(self) -> None:
        super().__init__()

    # Input string, output a list of strings shifted
    def shift(self, line):
        """Overrides CircularShifterInterface.shift()"""
        # add initial string
        output_list = np.array(line)

        # split original string into individual words
        temp = np.array(line.split(" "))

        # for as many permutations possible...
        for word in range(len(temp) - 1):
            # shift the previous array of words as prescribed
            temp = np.roll(temp, -1)

            # combine the resulting words to form a single string
            # and add it to the output
            output_list = np.append(output_list, ' '.join(temp))

        # convert the output np.array to simple list
        return output_list.tolist()
