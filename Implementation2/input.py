#Author: Sarthak Sanyasi
#implementation2 - input

from interface.input_interface import InputInterface


class Input(InputInterface):
    def get_data(self):
        """Overrides InputInterface.get_data()"""
        with open('input_file.txt', 'r') as file:
            lines = file.read().splitlines()
        file.close()
        return lines
