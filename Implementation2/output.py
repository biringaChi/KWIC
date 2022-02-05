#Author: Sarthak Sanyasi
#implementation2 - output

from typing import List

class Output:
    def output(self):
        with open('input_file') as file:
            for lines in file:
                print(lines.strip())
