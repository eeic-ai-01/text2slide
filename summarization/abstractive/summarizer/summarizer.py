from abc import ABCMeta, abstractmethod

class Summarizer(metaclass=ABCMeta):

    @abstractmethod
    def exec(self, text):
        pass
