import time
import re
import requests
import os
from pathlib import Path
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import TfidfVectorizer
from janome.tokenizer import Tokenizer
import json
import numpy as np



def scraping(rawtext, paragraph): #入力は一段落ずつ文字列でくる 
    t = Tokenizer()
    s_split = [token.surface for token in t.tokenize(rawtext)]
    docs = ' '.join(map(str, s_split)) # 分かち書き後の文字列
    

    # import json
    # Wikipediaデータセット読み込み
    Categories = ['animal', 'art', 'economy', 'law', 'plant', 'politics']

    with open('/home/u00417/text2slide/scraping/text/wikipedia_wakati.json', 'r', encoding='utf-8') as fi:
        wiki = json.load(fi)

    # Wikipediaデータセットの分かち書き作成

    wakati = []
    for cate in Categories:
        text = ''
        for item in wiki[cate]:
            for line in wiki[cate][item]['wakati']:
                text = text + line.replace('\n','') # 分かち書き文には改行記号が含まているので除去します
        wakati.append(text) 

    corpus = np.array(wakati)

    """
    for c in corpus:
        print(c[0:50])
    """

    arr_docs = np.array(docs)

    # 学習と重要語抽出
    # word_list = [] # 返す重要語のリスト

    corpus_article = np.append(corpus, arr_docs)
    print(corpus_article[6][0:50]) # 記事の内容を確認 corpus_article[0]〜[5]はWikipediaデータ

    vectorizer = TfidfVectorizer(max_features=10000, max_df=5, min_df=3)
    X = vectorizer.fit_transform(corpus_article)

    # print(X.shape) # Xの次元数を出力

    words = vectorizer.get_feature_names()
    
    important_word = [] # 返す重要語のリスト
    for doc_id, vec in zip(range(1+6), X.toarray()):
        if doc_id == 6:
            print('paragraph:', paragraph)
            paragraph += 1
            cnt=0
            for w_id, tfidf in sorted(enumerate(vec), key=lambda x: x[1], reverse=True):
                lemma = words[w_id]
                print('\t{0:s}: {1:f}'.format(lemma, tfidf))
                if not tfidf == 0:
                    important_word.append(lemma)
                cnt+=1
                if cnt==3:
                    break

    return important_word


def irasutoya(word_list, paragraph):#出力はその段落で使う画像のファイル名

    # print(word_list)
    
    output_folder = Path('out_png')
    output_folder.mkdir(exist_ok=True)
    search = 'https://www.irasutoya.com/search?q='
    
    flg = 0 # ダウンロードが成功したか
    
    print('')
    print('段落: ',paragraph)

    # ディレクトリがなかったら作成
    if not os.path.exists('out_png/'+ str(paragraph)):
        os.mkdir('out_png/' + str(paragraph))

    for cnt in range(len(word_list)):
        if flg == 1:
            break
        keyword = word_list[cnt]
        
        print('')
        print(keyword)
        
        url = search + keyword
        # 画像ページのURLを格納するリスト
        linklist = []


        html = requests.get(url).text
        soup = BeautifulSoup(html, 'lxml')
        a_list =soup.select('div.boxmeta.clearfix > h2 > a')
        # 画像リンクがない場合
        # 
        for a in a_list:
            link_url = a.attrs['href']
            linklist.append(link_url)
            time.sleep(0.3)
            
        
        for page_url in linklist:
            if flg == 1:
                break

            page_html = requests.get(page_url).text
            page_soup = BeautifulSoup(page_html, "lxml")
        # 画像ファイルのタグをすべて取得
            img_list = page_soup.select('div.entry > div > a > img')
            
            for img in img_list:
                img_url = (img.attrs['src'])
                filename = re.search(".*\/(.*png|.*jpg)$",img_url)
                save_path = output_folder.joinpath(str(paragraph), filename.group(1))
                print(filename, save_path)
                time.sleep(0.3)
                try:
                    image = requests.get(img_url)
                    open(save_path, 'wb').write(image.content)
                    print(keyword, save_path)
                    time.sleep(0.3)
                    flg = 1
                    print('successfully downloaded!')
                    return save_path
                    
                except ValueError:
                    print(keyword, "ValueError!")

    return None