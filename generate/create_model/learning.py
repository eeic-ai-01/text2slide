import random
import os
import fasttext as ft

model = ft.train_supervised(input="__in.txt", epoch=500, lr=0.7)
model.save_model("wikihow.model")

results = model.test("__out.txt")
print(results)