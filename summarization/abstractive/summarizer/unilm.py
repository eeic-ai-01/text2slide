from transformers import AutoTokenizer, AutoModel
import torch

class UniLM:
    def __init__(self):
        pass
    
    def exec(self, text):
        tokenizer = AutoTokenizer.from_pretrained("microsoft/unilm-base-cased")
        model = AutoModel.from_pretrained("microsoft/unilm-base-cased")
        inputs = tokenizer(text, return_tensors="pt")
        outputs = model(**inputs)
        return outputs[0]