__author__ = 'biringaChi'

from input import Input
from linestorage import LineStorage
from circular_shifter import CircularShifter
from alphabetizer import Alphabetizer
from output import Output


def main():
	linestorage = LineStorage() 

	input = Input().getData()
	linestorage.store_lines(input)

	shifted_lines = []
	for line in input:
		shifted_lines.append(CircularShifter().shift(line))

	linestorage.store_permutations(shifted_lines)
	aplhabetized = Alphabetizer().alphabetizer(shifted_lines)
	Output().output(aplhabetized)

if __name__ == "__main__":
	main()
	