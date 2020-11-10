import requests
import os
from .translater import Translater

class DeepLTransltator(Translater):
    def __init__(self):
        super().__init__()

    def _translate_to_en(self, text):
        return self.trans(text, 'JA', 'EN')

    def _translate_to_ja(self, text):
        return self.trans(text, 'EN', 'JA')
    
    def trans(self, text, frm, to):
        KEY = os.getenv("DEEPL_KEY")
        payload = {
            "auth_key": KEY,
            "text": text,
            "source_lang": frm, 
            "target_lang": to,
        }
        req = requests.post("https://api.deepl.com/v2/translate", data=payload)
        result = req.json()
        return result["translations"][0]["text"]