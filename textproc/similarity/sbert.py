from .similarity import Similarity
import transformers
transformers.BertTokenizer = transformers.BertJapaneseTokenizer

from sentence_transformers import SentenceTransformer
from sentence_transformers import models
from sklearn.metrics.pairwise import cosine_similarity


class SBert(Similarity):
    def __init__(self):
        pass

    def calc(self, text1, text2):
        transformer = models.BERT('cl-tohoku/bert-base-japanese-whole-word-masking')
        pooling = models.Pooling(transformer.get_word_embedding_dimension(), pooling_mode_mean_tokens=True, pooling_mode_cls_token=False, pooling_mode_max_tokens=False)
        model = SentenceTransformer(modules=[transformer, pooling])

        sentences = [text1, text2]
        embeddings = model.encode(sentences)

        return cosine_similarity([embeddings[0]], [embeddings[1]])[0][0]
