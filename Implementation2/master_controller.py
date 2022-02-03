from line_storage import LineStorage
from input import Input
from circular_shifter import CircularShifter
from alphabetizer import Alphabetizer
from output import Output


def main():
    storage = LineStorage()
    input = Input()
    shifter = CircularShifter()
    alphabetizer = Alphabetizer()
    output = Output()

    lines = input.get_data()

    storage.store_lines(lines)

    permutations = []
    for line in lines:
        permutations.append(shifter.shift(line))

    storage.store_permutations(permutations)

    output.output(alphabetizer.alphabetize(storage.get_permutations()))


if __name__ == '__main__':
    main()
