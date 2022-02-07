#Author: Sarthak Sanyasi
#implementation2 - output
from interface.output_interface import OutputInterface
from typing import List

class Output(OutputInterface):
    def __init__(self) -> None:
        super().__init__()
        
    def output(self, lines):
        """Overrides OutputInterface.output()"""
        with open('input_file') as file:
            for lines in file:
                print(lines.strip())
