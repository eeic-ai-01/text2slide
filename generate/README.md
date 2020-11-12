# colabでの実行
初回はupdate_pandoc.ipynbを走らせてください。
colabに入っているpandocのバージョンアップをさせるのですが、ネットの情報いわく40分程度（！）かかります。

そのあとはcolab.ipynbを走らせればよいです。

# ISTでの実行
## 必要なライブラリ

- pandoc
  - standaloneを含めてありますのでインストール不要です
- fasttext
  - pip install fasttextで取ってきたfasttextはうまく動きません。そのためgitで配布されているものをインストールします
  - すでにgitからcloneしてきたfastTextフォルダがあります。インストールするには
    - cd fastText
    - pip install .
  - してください。そのあと戻ってきてください
- janome
    - もうみんな知ってそうだけどIST環境ではpythonのバージョン的に最新のJanomeでは動かない
    - pip install Janome==0.3.10 だと動く

## 実行
generate_slide内で `python(3) prediction.py {原稿のテキストファイル} {変換用のmdファイル} {modelの名前}` してください。
推測されたカテゴリのうち上位3つのテーマでpptxが出力されます。
とりあえず `python(3) prediction.py script.txt out.md wikihow` で試せると思います。
modelは11/11 13時現在wikihowのものしかありません。{modelの名前}には基本的にwikihowを入れてください。

# 文法など
## 学習させるためのファイルは
今のところ含めてません。

## mdファイルの文法は
`python(3) prediction.py script.txt out.md wikihow` していただいて、
out.mdとslide_n.pptxを見比べていただければノリはつかめるかなと思います。
ちゃんとout.md書いていなくてすみません。
自動出力なので（？）文字数が多すぎるとテキストボックスから溢れてしまいます。文字数制限を要約側でかけたほうがいいかも