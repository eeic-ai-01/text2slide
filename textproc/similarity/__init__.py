from .sbert import SBert

def calc_similarity(text1, text2):
    model = SBert()
    return model.calc(text1, text2)
