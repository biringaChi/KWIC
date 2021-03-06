__author__ = 'biringaChi'

from typing import List
from interface.linestorage_interface import LineStorageInterface
from circular_shifter import CircularShifter

class LineStorage(LineStorageInterface, CircularShifter):
	"""Line Storage Implementation"""
	def __init__(self) -> None:
		super().__init__()
		self.CORE_LINES: List[str] = []
		self.PERMUTATIONS: List[str] = []

	def __str__(self) -> str: return {self.__class__.__name__}
	def __repr__(self) -> str: return self.__str__()
	
	def store_lines(self, lines: List[str]):
		"""Overrides LineStorageInterface.store_lines()"""
		self.CORE_LINES = lines
	
	def get_line(self, idx: int) -> str:
		"""Overrides LineStorageInterface.get_line()"""
		if (isinstance(idx, (int, float))): 
			return self.CORE_LINES[idx]
		else: raise TypeError("Invalid argument. Only 'ints' and 'floats' are accepted")
	
	def store_permutations(self, permutations):
		"""Overrides LineStorageInterface.store_permutations()"""
		self.PERMUTATIONS.append(permutations)
	
	def get_permutations(self) -> List[str]:
		"""Overrides LineStorageInterface.get_permutations()"""
		return self.PERMUTATIONS
	
	def get_permutation_index(self, idx: int) -> str:
		"""Overrides LineStorageInterface.get_permutation_index()"""
		if (isinstance(idx, (int))): 
			return self.PERMUTATIONS[idx]
		else: raise TypeError("Invalid argument. Only 'ints' are accepted")
