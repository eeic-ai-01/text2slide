こちらのフォルダはスライド作成には影響しませんが、ファイル `wikihow.model` を作るコードを格納しています。

## 使うライブラリ
fastTextです。

## 使うデータ
[wikihow](https://www.wikihow.jp/)をスクレイピングし、metaタグを読んで得られる概要の文章です。ご自身でご用意ください。

## 用意すべきデータの形式
fastTextでモデルを作る際、データはtxtファイルで用意する必要があります。

```
__label__a 病気 を 患っ て いる 時 、 九死 に...
__label__b 日々 の 生活 を 楽しむ こと も でき...
```

このように、スペースで分かち書きされ1行にまとめられた文章データの先頭に `__label__`で始まる（そのカテゴリを示す）ラベル名称がついている形式のものを用意します、
方法が多くあるのでわざわざコードにはしませんが、`bs4`や`janome`をhtml文書のスクレイピングや分かち書きで利用しました。
訓練用とテストようにデータを分けておく必要もあります、

## learning.py
学習を行うのはこのファイルのみのコードだけです。`epoch`や`lr`を変えて学習させられます。

## 公式ドキュメント
[こちらです](https://fasttext.cc/docs/en/supervised-tutorial.html)