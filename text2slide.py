from summarization.abstractive import summarize
from summarization.extractive.SlideMan.youyakuman import YouyakuMan
from scraping.scraping import scraping,irasutoya
from generate.generate import generate
import argparse
import sys
import textproc

import itertools

def preprocess(_document):
    document = _document.split('\n\n')
    document = [paragraph for paragraph in document if paragraph != '']
    return document


class PrintMarkdown:
    def __init__(self,outfile,titles,summaries,pictures):
        self.outfile = outfile
        self.titles = titles
        self.summaries = summaries
        self.pictures = pictures
        self.sections = sorted(summaries.keys())
        self.print_cover()
        self.print_pages()
    def print_cover(self):
        self.outfile.write("---\n")
        self.outfile.write("title: MarkdownでPowerPointスライド\n")
        self.outfile.write("subtitle: サブタイトル\n")
        self.outfile.write("author: 実験1班\n")
        self.outfile.write("---\n")
    def print_pages(self):
        def print_title(title):
            self.outfile.write("## %s\n" % (title))
        def print_sentences(sentences):
            for sentence in sentences:
                print(sentence)
                self.outfile.write("- %s\n" % (sentence))
        def print_picture(picture):
            self.outfile.write("![](%s)\n" % (picture))
        for i in self.sections:
            picture_path=self.pictures.get(i,None)
            print_title(self.titles[i])
            if picture_path: #画像がある場合
                self.outfile.write(":::::::::::::: {.columns}\n::: {.column width=\"50%\"}\n")
                print_sentences(self.summaries[i])
                self.outfile.write(":::\n::: {.column width=\"50%\"}\n")
                print_picture(self.pictures[i])
                self.outfile.write(":::\n::::::::::::::\n")
            else: #画像がない場合
                print_sentences(self.summaries[i])

            
def text2slide(document, output="output"):
    preprocessed_doc = preprocess(document)
    titles = {}
    contents = {}
    pictures = {}
    for i, paragraph in enumerate(preprocessed_doc):
        titles[i] = summarize.summarize(paragraph, 'google/pegasus-xsum')
        titles[i] = textproc.tiltlize(titles[i])
        titles[i] = textproc.desmasu2dadearu(titles[i])
        contents_extractive = YouyakuMan(paragraph,3) #リスト形式で指定した数（以上）の抽出した文が返される
        contents_abstractive = summarize.summarize(paragraph, 'google/pegasus-cnn_dailymail').split("。")
        contents_abstractive = filter(lambda x: x != '', contents_abstractive)

        contents_extractive = list(map(lambda x: textproc.desmasu2dadearu(x), contents_extractive))
        contents_abstractive = list(map(lambda x: textproc.desmasu2dadearu(x), contents_abstractive))

        SIMILARITY_TH = 88

        for j, text_ext in enumerate(contents_extractive):
            for text_abs in contents_abstractive:
                print(text_ext, ' / ', text_abs)
                similarity = textproc.calc_similarity(text_ext, text_abs)
                print(similarity)
                if similarity >= SIMILARITY_TH :
                    if (len(text_ext) > len(text_abs)):
                        contents_extractive[j] = text_abs
                
        contents[i] = contents_extractive
        pictures[i] = irasutoya(scraping(paragraph,i),i) #あってる
    print("summarization result:\n---")
    print(titles)
    print(contents)
    print("----")
    with open(output + ".md", mode='w', encoding='utf8', buffering=1) as outfile:
        PrintMarkdown(outfile,titles,contents,pictures)
    generate(document, output)

def main():
    parser = argparse.ArgumentParser(description="")
    parser.add_argument("--input", "-i", type=str, required=True, help="")
    parser.add_argument("--output", "-o", type=str, default="output", help="")
    args = parser.parse_args()
    input = args.input
    output = args.output
    document = ""
    with open(input, mode='r', encoding='utf8') as f:
        document = f.read()
    text2slide(document, output)

if __name__ == "__main__":
    main()
    
   
