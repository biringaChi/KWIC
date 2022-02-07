#Author: Sarthak Sanyasi
#implementation2 - input

class Input:
    # to maintain OOD, to make static delete constructor
    def __init__(self):
        pass

    def get_data(self):
        with open('input_file.txt', 'r') as f:
            lines = f.read().splitlines()
        f.close()
        return lines
