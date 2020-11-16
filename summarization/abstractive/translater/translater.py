from abc import ABCMeta, abstractmethod
from dotenv import load_dotenv
import hashlib
import pickle
import atexit

class Translater(metaclass=ABCMeta):

    def __init__(self):
        load_dotenv()

        try:
            with open(f"{self.__class__.__name__}_cache.pkl", "rb") as f:
                self.cache = pickle.load(f)
        except FileNotFoundError:
            self.cache = {}
        
        def save_pkl(name):
            with open(f"{name}_cache.pkl", "wb") as f:
                pickle.dump(self.cache, f)
        
        atexit.register(save_pkl, self.__class__.__name__)
    
    def translate_to_ja(self, text):
        if self.hash(text) in self.cache:
            return self.cache[self.hash(text)] 
        else:
            result = self._translate_to_ja(text)
            self.cache[self.hash(text)] = result
            self.cache[self.hash(result)] = text
            return result

    def translate_to_en(self, text):
        if self.hash(text) in self.cache:
            return self.cache[self.hash(text)] 
        else:
            result = self._translate_to_en(text)
            self.cache[self.hash(text)] = result
            self.cache[self.hash(result)] = text
            return result

    @staticmethod
    def hash(text):
        return hashlib.md5(text.encode()).hexdigest()

    @abstractmethod
    def _translate_to_ja(self, text):
        pass

    @abstractmethod
    def _translate_to_en(self, text):
        pass
