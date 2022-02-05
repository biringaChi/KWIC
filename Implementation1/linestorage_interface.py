__author__ = 'biringaChi'

from typing import List

class LineStorageInterface:
	"""
	Line Storage Interface
	"""

	def store_lines(self) -> None:
		"""Store retrieved data in a data structure"""
		pass

	def get_line(self, idx: int) -> str:
		"""Get a specific line at a given index"""
		pass

	def store_permutations(self) -> None:
		"""Store permutated data"""
		pass
	
	def get_permutations(self) ->  List[str]:
		"""Get all permutated lines"""
		pass

	def get_permutation_index(self, idx: int) -> str:
		"""Get a specific permutated line at a given index"""
		pass