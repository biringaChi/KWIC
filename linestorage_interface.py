__author__ = 'biringaChi'

from typing import Dict, List

class LineStorageInterface:
	"""
	Line Storage Interface
	"""

	def get_data(self) -> List[str]:
		"""Get loaded data from input module"""
		pass

	def store_lines(self) -> Dict[int, str]:
		"""Store retrieved data in a data structure"""
		pass

	def get_line(self, idx: int) -> str:
		"""Get a specific line at a given index"""
		pass
	
	def get_permutations(self) ->  List[str]:
		"""Get all permutated lines"""
		pass

	def get_permutation_index(self, idx: int) -> str:
		"""Get a specific permutated line at a given index"""
		pass