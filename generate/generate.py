# -*- coding: utf-8 -*-

# ルートディレクトリでの実行を想定しているため任意のもののパスはルートから

import re
import sys
import subprocess
import fasttext as ft
from janome.tokenizer import Tokenizer

model_name = "wikihow"

def generate(document, output):
    document = document.replace("\r\n", "")
    document = document.replace("\n", "")
    document = document.replace("\u3000", "")
    document = wakati(document)
    model = ft.load_model("./generate/" + model_name + ".model")
    labels, probs = model.predict(document.strip(), k=3)

    rank = 0
    print("generating start")
    for label, prob in zip(labels, probs):
        category = label.replace("__label__", "")
        print("{0} category = {1} (probability = {2}) generating...".format(rank, category, prob))
        rank += 1
        subprocess.call(["./generate/pandoc", output + ".md", "-o", "{0}_{1}.pptx".format(output, rank), "--reference-doc=./generate/templates/{0}/{1}.pptx".format(model_name, category)])
    print("finished")

def wakati(text):
    t = Tokenizer()
    w = t.tokenize(text, wakati=True)
    return ' '.join(w)