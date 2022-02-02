__author__ = 'biringaChi'

from typing import List
from linestorage_interface import LineStorageInterface
from circular_shifter import CircularShifter
from input import getData 

class LineStorage(LineStorageInterface, CircularShifter):
	"""Line Storage Implementation"""
	def __init__(self) -> None:
		super().__init__()

	def __str__(self) -> str: return {self.__class__.__name__}
	def __repr__(self) -> str: return self.__str__()

	def load_dummy_data(self) -> List[str]:
		"""Place holder for getData()"""
		with open("dummy.txt") as dummy_data:
			data = dummy_data.readlines()
		return data

	def get_data(self) -> List[str]:
		"""Overrides LineStorageInterface.get_data()"""
		return self.load_dummy_data()
	
	def store_lines(self) -> List[str]:
		"""Overrides LineStorageInterface.store_lines()"""
		""" We store lines and correspoding indexes in a dictionary
			This is just an example, we can use any data structure or object to store the lines
		"""
		return {idx: lines for idx, lines in enumerate(self.load_dummy_data())}
	
	def get_line(self, idx: int) -> str:
		"""Overrides LineStorageInterface.get_line()"""
		if (isinstance(idx, (int, float))): 
			return self.store_lines()[idx]
		else: raise TypeError("Invalid argument. Only 'ints' and 'floats' are accepted")
	
	def store_permutations(self) -> List[str]:
		"""Overrides LineStorageInterface.store_permutations()"""
		permutations: List[str] = self.shift()
		return permutations
	
	def get_permutations(self) -> List[str]:
		"""Overrides LineStorageInterface.get_permutations()"""
		return self.store_permutations()
	
	def get_permutation_index(self, idx) -> str:
		"""Overrides LineStorageInterface.get_permutation_index()"""
		shifted_lines = self.shift("This is my input string")
		if (isinstance(idx, (int))): 
			return shifted_lines[idx]
		else: raise TypeError("Invalid argument. Only 'ints' are accepted")