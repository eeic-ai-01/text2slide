# text2slide

## モデルなどの導入(抽出型要約について)
### BERT日本語pretrainモデルの読み込み
[BERT日本語Pretrainedモデル — KUROHASHI-KAWAHARA LAB](http://nlp.ist.i.kyoto-u.ac.jp/index.php?BERT日本語Pretrainedモデル)
からBASE WWM版(1.6G; 19/11/15公開)をダウンロードして展開し、中身をsummarization/extractive/SlideMan/model/Japanese/に置く。
summarization/extractive/SlideMan/src/LangFactory.pyの46行目にその絶対パスを入力する。
### Jumanのインストール
[Juman++ V2の開発版](https://github.com/ku-nlp/jumanpp)に記載された通りに2.0.0-rc3をインストールする。
summarization/extractive/SlideMan/config.iniに、jumanpp、vocab.txt、jumandic.jppmdl、jumandic.configの絶対パスを入力する。
### wikihowデータにより学習させたモデルの読み込み
〇〇からcp_step_9000.ptとopt_step_9000.ptをダウンロードし、summarization/extractive/SlideMan/checkpoint/jp/に置く。
summarization/extractive/SlideMan/src/LangFactory.pyの50行目、51行目にその絶対パスを入力する。

