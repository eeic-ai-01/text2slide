import os
import argparse
from argparse import RawTextHelpFormatter

from .src.TestLoader import TestLoader
from .src.ModelLoader import ModelLoader
from .src.Summarizer import SummarizerIO
from .src.Translator import TranslatorY
from .src.LangFactory import LangFactory
from .src.PicturePicker import PicturePicker
from .src.PrintMarkdown import PrintMarkdown

os.chdir('./')

class Settings:
    def __init__(self,n=3,lang="jp",super_long=True):
        self.super_long=super_long
        self.lang=lang 
        self.n=n

def YouyakuMan(rawtext,n=3):
    args=Settings(n)
    lf = LangFactory(args.lang)
    translator = None if args.lang in lf.support_lang else TranslatorY()
    data = TestLoader(rawtext, args.super_long, args.lang, translator).data
    model = ModelLoader(lf.toolkit.cp, lf.toolkit.opt, lf.toolkit.bert_model)
    summarizer = SummarizerIO(data, model, args.n,translator)
    return summarizer.summaries


if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter,
                                     description="""
    Intro:   This is an one-touch extractive summarization machine.
             using BertSum as summatization model, extract top N important sentences.

    Note:    Since Bert only takes 512 length as inputs, this summarizer crop articles >512 length.
             If --super_long option is used, summarizer automatically parse to numbers of 512 length
             inputs and summarize per inputs. Number of extraction might slightly altered with --super_long used.

    Example: youyakuman.py -txt_file YOUR_FILE -n 3
    """)

    parser.add_argument("-txt_file", default='test.txt',
                        help='Text file for summarization (encoding:"utf-8_sig")')
    parser.add_argument("-n", default=3, type=int,
                        help='Numbers of extraction summaries')
    parser.add_argument("-lang", default='en', type=str,
                        help='If language of article isn\'t Englisth, will automatically translate by google')
    parser.add_argument("--super_long", action='store_true',
                        help='If length of article >512, this option is needed')

    args = parser.parse_args()

#    if args.super_long:
#        sys.stdout.write('\n<Warning: Number of extractions might slightly altered since with --super_long option>\n')

    # Language initiator
    lf = LangFactory(args.lang)
    translator = None if args.lang in lf.support_lang else TranslatorY()
    # 段落分け
    with open(args.txt_file, 'r', encoding='utf-8_sig', errors='ignore') as f:
        rawtexts = f.read()
    rawtexts=rawtexts.split("\n\n")
    #画像の提示
    #ppicker=PicturePicker(rawtexts)
    #ppicker.savepictures()
    #pictures=ppicker.picture_paths
    pictures = {}
    for i in range(10):
        pictures[i]=None
    #要約の提示
    summaries={}
    for i,rawtext in enumerate(rawtexts):
        data = TestLoader(rawtext, args.super_long, args.lang, translator).data
        model = ModelLoader(lf.toolkit.cp, lf.toolkit.opt, lf.toolkit.bert_model)
        summarizer = SummarizerIO(data, model, args.n,translator)
        summaries[i]=summarizer.summaries
    print(summaries)
    #　タイトルの提示
    titles = {}
    for i in range(10):
        titles[i]="タイトル"
    #プリントアウト
    with open("output1.md", mode='w', encoding='utf8', buffering=1) as outfile:
        PrintMarkdown(outfile,titles,summaries,pictures)
