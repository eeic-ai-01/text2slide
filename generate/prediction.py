# -*- coding: utf-8 -*-

# this program is outdated. 

import re
import sys
import subprocess
import fasttext as ft
from janome.tokenizer import Tokenizer

def main():
    if len(sys.argv) < 4:
        print("3 arguments(script, md, model) required")
        return
    script = sys.argv[1]
    script_name = re.sub('\..*', '', script)
    md = sys.argv[2]
    model = sys.argv[3]

    # colaboratoryのときのみ動作
    is_colab = sys.argv[4] if len(sys.argv) > 4 else None

    mod = ft.load_model(model + ".model")
    with open(script, "r") as f:
        text = f.read()
        text = text.replace("\r\n", "")
        text = text.replace("\n", "")
        text = text.replace("\u3000", "")
        text = wakati(text)
        print(text)
        labels, probs = mod.predict(text.strip(), k=3)
        rank = 1
        for label, prob in zip(labels, probs):
            category = label.replace("__label__", "")
            print("{0} category = {1} (probability = {2}) generating...".format(rank, category, prob))
            if is_colab == "colab":
                subprocess.call(["/root/.local/bin/pandoc", md, "-o", "{0}_{1}.pptx".format(script_name, rank), "--reference-doc=./templates/{0}/{1}.pptx".format(model, category)])
            else:
                subprocess.call(["./pandoc", md, "-o", "{0}_{1}.pptx".format(script_name, rank), "--reference-doc=./templates/{0}/{1}.pptx".format(model, category)])
            rank += 1
        print("finished")

def wakati(text):
    t = Tokenizer()
    w = t.tokenize(text, wakati=True)
    return ' '.join(w)

if __name__ == '__main__':
    main()