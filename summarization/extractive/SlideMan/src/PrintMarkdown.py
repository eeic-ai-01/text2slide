
import sys

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
        self.outfile.write("title: タイトル\n")
        self.outfile.write("subtitle: サブタイトル\n")
        self.outfile.write("author: 実験1班\n")
        self.outfile.write("---\n")
    def print_pages(self):
        def print_title(title):
            self.outfile.write("## %s\n" % (title))
        def print_sentences(sentences):
            for sentence in sentences:
                self.outfile.write("- %s\n" % (sentence))
        def print_picture(picture):
            self.outfile.write("![](%s)\n" % (picture))
        for i in self.sections:
            picture_path=self.pictures.get(i,None)
            print_title(self.titles[i])
            if picture_path: #画像がある場合
                self.outfile.write(":::::::::::::: \{.columns\}\n::: \{.column width=\"65%\"\}\n")
                print_sentences(self.summaries[i])
                self.outfile.write(":::\n::: \{.column width=\"35%\"\}\n")
                print_picture(self.pictures[i])
                self.outfile.write(":::\n::::::::::::::\n")
            else: #画像がない場合
                print_sentences(self.summaries[i])

            