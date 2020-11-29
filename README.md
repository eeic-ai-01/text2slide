# text2slide

## 環境構築

Python 3.8.6で動作を確認しています

```
$ git clone https://github.com/eeic-ai-01/text2slide --recursive
$ cd text2slide
$ pip install -r requirements.txt
$ python -m spacy download en
```

pyenv環境の場合fasttextのみ手動でインストール必要があります．
```
$ git clone https://github.com/facebookresearch/fastText.git
$ cd fastText
$ pip install .
```

### [pandoc](https://pandoc.org)のインストール
https://pandoc.org/installing.html

### モデルなどの導入(抽出型要約について)
#### BERT日本語pretrainモデルの読み込み
[BERT日本語Pretrainedモデル — KUROHASHI-KAWAHARA LAB](http://nlp.ist.i.kyoto-u.ac.jp/index.php?BERT日本語Pretrainedモデル)
からBASE WWM版(1.6G; 19/11/15公開)をダウンロードして展開し、中身をsummarization/extractive/SlideMan/model/Japanese/に置く。
summarization/extractive/SlideMan/src/LangFactory.pyの46行目にその絶対パスを入力する。
#### Jumanのインストール
[Juman++ V2の開発版](https://github.com/ku-nlp/jumanpp)に記載された通りに2.0.0-rc3をインストールする。
summarization/extractive/SlideMan/config.iniに、jumanpp、vocab.txt、jumandic.jppmdl、jumandic.configの絶対パスを入力する。
#### wikihowデータにより学習させたモデルの読み込み
〇〇からcp_step_9000.ptとopt_step_9000.ptをダウンロードし、summarization/extractive/SlideMan/checkpoint/jp/に置く。
summarization/extractive/SlideMan/src/LangFactory.pyの50行目、51行目にその絶対パスを入力する。

### DeepL API キーの登録
一部の要約に英語向けのモデルを使用しているため`.env`にDeepL APIを登録する必要があります．

