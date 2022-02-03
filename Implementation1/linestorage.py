__author__ = 'biringaChi'

from typing import List
from linestorage_interface import LineStorageInterface
from circular_shifter import CircularShifter
# from input import getData 

class LineStorage(LineStorageInterface, CircularShifter):
	"""Line Storage Implementation"""
	def __init__(self) -> None:
		super().__init__()
		self.LINES: List[str] = []
		self.PERMUTATIONS: List[str] = []

	def __str__(self) -> str: return {self.__class__.__name__}
	def __repr__(self) -> str: return self.__str__()
	
	def store_lines(self, lines: List[str]):
		"""Overrides LineStorageInterface.store_lines()"""
		self.LINES.append(lines)
	
	def get_line(self, idx: int) -> str:
		"""Overrides LineStorageInterface.get_line()"""
		if (isinstance(idx, (int, float))): 
			return self.store_lines()[idx]
		else: raise TypeError("Invalid argument. Only 'ints' and 'floats' are accepted")
	
	def store_permutations(self):
		"""Overrides LineStorageInterface.store_permutations()"""
		permutations: List[str] = self.shift()
		self.PERMUTATIONS.append(permutations)
	
	def get_permutations(self) -> List[str]:
		"""Overrides LineStorageInterface.get_permutations()"""
		return self.store_permutations()
	
	def get_permutation_index(self, idx: int) -> str:
		"""Overrides LineStorageInterface.get_permutation_index()"""
		shifted_lines = self.shift("This is my input string")
		if (isinstance(idx, (int))): 
			return shifted_lines[idx]
		else: raise TypeError("Invalid argument. Only 'ints' are accepted")