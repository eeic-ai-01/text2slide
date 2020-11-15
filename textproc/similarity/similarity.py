from abc import ABCMeta, abstractmethod

class Similarity(metaclass=ABCMeta):

    @abstractmethod
    def calc(self, text1, text2):
        pass
