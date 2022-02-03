'''

Author:
    Alexander J. Moulton
    Github: @moul-10

Usage:
    short_word = Word("big")
    string_short_word = short_word.get_content()
    short_word.set_content("red")

'''

class Word:
    def __init__(self, content: str):
        self.__content = content

    def set_content(self, content: str):
        self.__content = content

    def get_content(self) -> str:
        return self.__content
