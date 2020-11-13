from janome.tokenizer import Tokenizer
import re

def wakatize(text):
    tokenizer = Tokenizer()
    wakati = []
    dic = []
    for token in tokenizer.tokenize(text):
        wakati.append(token.surface)
        dic.append(token)
        # surface / part_of_speech, infl_type, infl_form, base_form, reading, phonetic
        
    return wakati, dic
