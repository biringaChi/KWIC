# Grady Landers
# KWIC Implementation 1 - Output module

class Output:
    # output(List<String>): void
    # In this implementation, output() prints a number of strings to the console
    @staticmethod
    def output(lines):
        print("Results:")
        for line in lines:
            print(line)
