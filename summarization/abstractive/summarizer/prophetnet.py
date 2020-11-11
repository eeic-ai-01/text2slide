from transformers import ProphetNetTokenizer, ProphetNetForConditionalGeneration, ProphetNetConfig
import torch

class ProphetNet:
    def __init__(self):
        pass
    
    def exec(self, text):
        model = ProphetNetForConditionalGeneration.from_pretrained('microsoft/prophetnet-large-uncased-cnndm')
        tokenizer = ProphetNetTokenizer.from_pretrained('microsoft/prophetnet-large-uncased-cnndm')

        # inputs = tokenizer([text], max_length=100, return_tensors='pt')
        inputs = tokenizer([text], return_tensors='pt')

        # Generate Summary
        summary_ids = model.generate(inputs['input_ids'], num_beams=14, max_length=512, early_stopping=True)
        tgt_text = tokenizer.batch_decode(summary_ids, skip_special_tokens=True)
        return tgt_text[0].replace('[X_SEP] ', '\n')
