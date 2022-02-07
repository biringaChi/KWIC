#Author: Sarthak Sanyasi
#implementation2 - input

from interface.input_interface import InputInterface

class Input(InputInterface):
    def get_data(self):
        """Overrides InputInterface.get_data()"""
        with open('input_file') as file:
            lines = file.readlines()
            return lines
