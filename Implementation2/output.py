#Author: Sarthak Sanyasi
#implementation2 - output
import os
from interface.output_interface import OutputInterface
from typing import List

class Output(OutputInterface):
    def __init__(self) -> None:
        super().__init__()
        
    def output(self, lines: List[str]):
        dir_name = os.path.dirname(__file__)
        file_name = os.path.join(dir_name, 'output_file.txt')

        # if output file already exists, remove it
        if os.path.exists(file_name):
            os.remove(file_name)
        # once removed, recreate it and append each line to it
        with open('output_file.txt', 'a+') as f:
            for line in lines:
                f.write(line + '\n')
        f.close()
