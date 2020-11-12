from summarization.abstractive import summarize
from summarization.extractive.SlideMan.youyakuman import YouyakuMan
from scraping.scraping import scraping,irasutoya
import argparse
import sys

def preprocess(_document):
    document = _document.split('\n')
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
        self.outfile.write("author:　実験1班\n")
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
    output += ".md"
    preprocessed_doc = preprocess(document)
    titles = {}
    contents = {}
    pictures = {}
    for i, paragraph in enumerate(preprocessed_doc):
        titles[i] = summarize.summarize(paragraph, 'google/pegasus-xsum')
        contents[i] = YouyakuMan(paragraph,3) #リスト形式で指定した数（以上）の抽出した文が返される
        pictures[i] = irasutoya(scraping(paragraph,i),i) #あってる
    with open(output, mode='w', encoding='utf8', buffering=1) as outfile:
        PrintMarkdown(outfile,titles,contents,pictures)

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
    
   
