__author__ = 'biringaChi'

from typing import List
from interface.alphabetizer_interface import AlphabetizerInterface

class Alphabetizer(AlphabetizerInterface):
	def __init__(self) -> None:
		super().__init__()

	def alphabetize(self, shifted_lines: List[str]):
		# the "sorted" function uses ASCII code
		return sorted(shifted_lines)