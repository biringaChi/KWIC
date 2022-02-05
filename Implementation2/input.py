#Author: Sarthak Sanyasi
#implementation2 - input

class Input:
    def getData(self):
        with open('input_file') as file:
            lines = file.readlines()
            return lines
