from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

class T5:
    def __init__(self):
        pass
    
    def exec(self, text):
        torch_device = 'cuda' if torch.cuda.is_available() else 'cpu'

        model = T5ForConditionalGeneration.from_pretrained('t5-11b', use_cdn = False).to(torch_device)
        tokenizer = T5Tokenizer.from_pretrained('t5-11b', return_dict=True)
        batch = tokenizer.prepare_seq2seq_batch(f"summarize: {text}", truncation=True, padding='longest').to(torch_device)
        outputs = model.generate(**batch)
        tgt_text = tokenizer.batch_decode(outputs, skip_special_tokens=True)
        print(tgt_text)
        return tgt_text[0]