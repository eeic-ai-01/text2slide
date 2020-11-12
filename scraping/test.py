import scraping

rawtext = 'スライド作成には大きな労力が必要です。プレゼン発表の前はただでさえ内容確認、Q&A対策、などの準備に追われているのに、発表用のスライドも用意しなくてはなりません。しかも、スライド作成はすぐに終わる作業ではなく、大きな手間を必要とします。 \
まず、発表内容から要点だけを抽出しなくてはなりません。原稿そのままの文章をスライドに載せてしまうと非常に見にくく、またどの部分に着目したら良いかもわからないため聞いている人に上手く伝えることができません。 \
また、その内容に合うグラフやイラストも用意する必要があります。視覚的に聞いている人に訴えかけることは大切な手法の一つです。 \
さらに、文章と画像をいい感じにスライドに配置する必要もあります。 \
最後に、テンプレートを選択する必要があります。'

word_list = scraping.scraping(rawtext, 1)
print(word_list)

path = scraping.irasutoya(word_list, 1)
print(path)