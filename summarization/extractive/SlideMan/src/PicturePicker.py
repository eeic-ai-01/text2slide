from sklearn.feature_extraction.text import TfidfVectorizer
from janome.tokenizer import Tokenizer
import time
import re
import requests
import os
from pathlib import Path
from bs4 import BeautifulSoup

class PicturePicker:#保存した画像のpathをself.picturepathに保存する
    def __init__(self,rawtexts):
        self.t = Tokenizer()
        self.rawtexts=rawtexts
    def savepictures(self):
        self.eval_words()
        self.pick_pictures()
        print(self.picture_paths)
    def eval_words(self):
        split_docs = []
        for s in self.rawtexts:
            s_split = [token.surface for token in self.t.tokenize(s) if token.part_of_speech.startswith('名詞')]
            split_docs.append(' '.join(map(str, s_split)))
        # print(split_docs)

        docs = split_docs
        vectorizer = TfidfVectorizer(max_df=0.9) # tf-idfの計算
        #                            ^ 文書全体の90%以上で出現する単語は無視する
        X = vectorizer.fit_transform(docs)

        words = vectorizer.get_feature_names()
        word_list = []
        for doc_id, vec in zip(range(len(docs)), X.toarray()):
            #print('doc_id:', doc_id)
            cnt=0
            important_word = []
            for w_id, tfidf in sorted(enumerate(vec), key=lambda x: x[1], reverse=True):
                lemma = words[w_id]
                #print('\t{0:s}: {1:f}'.format(lemma, tfidf))
                important_word.append(lemma)
                cnt+=1
                if cnt==3:
                    break
            word_list.append(important_word)
        self.word_list=word_list
        #print(word_list)
    def pick_pictures(self):
        self.picture_paths={}
        # ①-②.出力フォルダを作成
        output_folder = Path('いらすとや')
        output_folder.mkdir(exist_ok=True)
        # ①-③.スクレイピングしたいURLを設定
        search = 'https://www.irasutoya.com/search?q='
        doc_id = 0
        for section_number,words in enumerate(self.word_list):
            flg = 0 # ダウンロードが成功したか
            print('')
            doc_id+=1
            print('段落: ',doc_id)
            #os.mkdir('いらすとや/'+ str(doc_id))
            output_folder2 = Path('いらすとや/'+ str(doc_id))
            output_folder2.mkdir(exist_ok=True)
            for cnt in range(len(words)):
                if flg == 1:
                    break
                keyword = words[cnt]
                # keyword = words[0]
                print('')
                print(keyword)
                
                url = search + keyword
                # ①-④.画像ページのURLを格納するリストを用意
                linklist = []

                #●検索結果ページから画像のリンクを取り出す
                # ②-①.検索結果ページのhtmlを取得
                html = requests.get(url).text
                # ②-②.検索結果ページのオブジェクトを作成
                soup = BeautifulSoup(html, 'lxml')
                # ②-③.画像リンクのタグをすべて取得
                a_list =soup.select('div.boxmeta.clearfix > h2 > a')
                # ②-④.画像リンクを1つずつ取り出す
                # 画像リンクがない場合
                # 
                for a in a_list:
                # ②-⑤.画像ページのURLを抽出
                    link_url = a.attrs['href']
                # ②-⑥.画像ページのURLをリストに追加
                    linklist.append(link_url)
                    time.sleep(0.3)
                    
                # ●各画像ページから画像ファイルのURLを特定  
                
                # ③-①.画像ページのURLを1つずつ取り出す
                for page_url in linklist:
                    if flg == 1:
                        break
                # ③-②.画像ページのhtmlを取得
                    page_html = requests.get(page_url).text
                # ③-③.画像ページのオブジェクトを作成
                    page_soup = BeautifulSoup(page_html, "lxml")
                # ③-④.画像ファイルのタグをすべて取得
                    img_list = page_soup.select('div.entry > div > a > img')
                    
                # ③-⑤.imgタグを1つずつ取り出す
                    for img_num,img in enumerate(img_list):
                # ③-⑥.画像ファイルのURLを抽出
                        img_url = (img.attrs['src'])
                # ③-⑦.画像ファイルの名前を抽出
                        filename = re.search(".*\/(.*png|.*jpg)$",img_url)
                # ③-⑧.保存先のファイルパスを生成
                        save_path = output_folder.joinpath(str(doc_id), filename.group(1))
                        print(filename, save_path)
                        time.sleep(0.3)
                # ●画像ファイルのURLからデータをダウンロード
                        try:
                # ④-①.画像ファイルのURLからデータを取得
                            image = requests.get(img_url)
                # ④-②.保存先のファイルパスにデータを保存
                            open(save_path, 'wb').write(image.content)
                # ④-③.保存したファイル名を表示
                            print(keyword, save_path)
                            time.sleep(0.3)
                            flg = 1
                            print('successfully downloaded!')
                            if(img_num==0):
                                self.picture_paths[section_number]=save_path
                        except ValueError:
                # ④-④.失敗した場合はエラー表示
                            print(keyword, "ValueError!")