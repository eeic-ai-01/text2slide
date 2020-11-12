from transformers import PegasusForConditionalGeneration, PegasusTokenizer
import torch

class Pegasus:
    def __init__(self, model):
        self.model = model
    
    def exec(self, text):
        src_text = [text]
        model_name = self.model
        #model_name = 'google/pegasus-xsum'
        #model_name = 'google/pegasus-large'
        #model_name = 'google/pegasus-cnn_dailymail'
        #model_name = 'google/pegasus-pubmed'
        #model_name = 'google/pegasus-wikihow'
        #model_name = 'google/pegasus-newsroom'
        #model_name = 'google/pegasus-multi_news'
        #model_name = 'google/pegasus-reddit_tifu'
        #model_name = 'google/pegasus-arxiv'

        torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'
        tokenizer = PegasusTokenizer.from_pretrained(model_name)
        model = PegasusForConditionalGeneration.from_pretrained(model_name).to(torch_device)
        batch = tokenizer.prepare_seq2seq_batch(src_text, truncation=True, padding='longest').to(torch_device)
        result = model.generate(**batch)
        tgt_text = tokenizer.batch_decode(result, skip_special_tokens=True)

        return tgt_text[0]