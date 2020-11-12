import torch

from .utils.utils import DictX
from .models.model_builder import Summarizer


class ModelLoader(Summarizer):
    def __init__(self, cp, opt, bert_model):
        cp_statedict = torch.load(cp, map_location=lambda storage, loc: storage)
        opt = DictX(vars(torch.load(opt)))
        #opt = DictX(torch.load(opt))
        super(ModelLoader, self).__init__(opt, bert_model)
        self.load_cp(cp_statedict)
        self.eval()
