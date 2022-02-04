# Grady Landers
# KWIC Implementation 1 - Input module

class Input:
    # getData(): List<String>
    # In this implementation, getData() collects a number of strings from the keyboard
    # to be returned to the method caller
    @staticmethod
    def getData():
        lines = []
        print("Enter lines to be processed by the KWIC program. Enter an empty line to finish:")

        collecting = True
        while collecting:
            s = input()
            if s == "":
                collecting = False
            else:
                lines.append(s)

        return lines
