class Word:
    def __init__(self, content: str):
        self.__content = content

    def set_content(self, content: str):
        self.__content = content

    def get_content(self) -> str:
        return self.__content
