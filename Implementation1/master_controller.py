__author__ = 'biringaChi'

from input import Input
from linestorage import LineStorage
from circular_shifter import CircularShifter
from alphabetizer import Alphabetizer
from output import Output


def main():
	linestorage = LineStorage() 

	inputter = Input()
	input = inputter.get_data()
	linestorage.store_lines(input)

	shifted_lines = []
	for line in input:
		shifted_lines.append(CircularShifter().shift(line))

	linestorage.store_permutations(shifted_lines)

	shifted_lines_flat = [line for list_of_lines in shifted_lines for line in list_of_lines]

	alphabetizer = Alphabetizer()

	alphabetized = alphabetizer.alphabetize(shifted_lines_flat)

	Output().output(alphabetized)


if __name__ == "__main__":
	main()
	