# Grady Landers
# KWIC Implementation 1 - Output module
from interface.output_interface import OutputInterface

class Output(OutputInterface):
    # output(List<String>): void
    # In this implementation, output() prints a number of strings to the console
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def output(lines):
        """Overrides OutputInterface.output()"""
        print("Results:")
        for line in lines:
            print(line)
