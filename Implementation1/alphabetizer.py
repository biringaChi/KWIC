# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


#author: Sarthak Sanyasi
#usage: Alphabetizer function

from typing import List
import numpy as np
from interface.alphabetizer_interface import AlphabetizerInterface


class Alphabetizer(AlphabetizerInterface):
  
    def __init__(self) -> None:
        super().__init__()

    def alphabetize(self, output_list: List[str]):
        """Overrides AlphabetizerInterface.alphabetize()"""
        return np.sort(output_list)
