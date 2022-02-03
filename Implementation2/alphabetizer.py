__author__ = 'biringaChi'

from typing import List

class Alphabetizer:
	def __init__(self) -> None: pass

	def alphabetize(self, shifted_lines: List[str]):
		# the "sorted" function uses ASCII code
		return sorted(shifted_lines)