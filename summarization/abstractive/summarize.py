if __package__ is None or __package__ == '':
    import summarizer
    import translater
else:
    from . import summarizer
    from . import translater
    import textproc

trans = translater.DeepLTransltator()

def summarize(text, model):
    if 'pegasus' in model:
        ag = summarizer.Pegasus(model)
    elif 'prophetnet' in model:
        ag = summarizer.ProphetNet()
    else :
        ag = summarizer.Pegasus("google/pegasus-cnn_dailymail")

    src = text
    trc = trans.translate_to_en(src)
    strc = ag.exec(trc)
    print(strc)
    strc = textproc.sanitize(strc.split('.'))
    strc = '. '.join(strc)
    print(strc)
    result = trans.translate_to_ja(strc)
    print(result)
    
    return result

def main():
    #text = "こういう世の中だからね，一応生活には不自由しないし皆んな何をやっていいかよくわからない．よくいうでしょう，研究テーマを見つけることが半分以上，テーマが決まったあとは肉体的に苦しくても精神的にはものすごく楽なんだ．忙しいときは楽なんだよ．暇なときが一番苦しい．『夢を描く』ことを商売とするのは非常に大変だ．研究には夢がなくてはいけないが，これは話が反対だ．夢のない研究はむなしい．いま，あなたの夢を語れと言われて，一つも言えない人は研究者には向かない．極端にいえば，次に何をしようかと考えること以外は全部雑用だ．ところが雑用も結構楽しい．僕の場合だと，講義や講演でみんなに自分の考えを伝えること，学会の活動をすることみな楽しい．だからそれにおぼれてしまってね，本当に大切なことを見失ってしまうのだ．優等生を止めてサボリマンになろう．もちろん本当にサボってはいけないよ．研究は全部自分でやるんだよ．指導教官は一番身近にいるライバルだ．博士課程は，ほとんど制約のない状態で，さて自分は何をしようかを考え，それを組み立てる人生唯一のチャンスだ．人間の真価はそこで決まる．そのために，高い学費を払ってひとかたまりの時間を買うのだ．ぼんやり過ごすためではないのだ．エンジニアの給料が安いことや，経済的に自立できないことが博士課程に行く意欲をそいでいるのは事実だから，われわれは真剣に考えないといけないが，実際には修士・博士の５年間のロスは，あっという間に取り戻すことができる．学部で就職しても５年くらいはあれよあれよという間に過ぎてしまう．婚期が遅れるって心配する奴がいるけど，学生時代に恋人のひとりもいない奴は，どうせ晩婚だよ．だいたい相手が欲しいと思っていていないのは，極端にいえば努力が足りないんだからいなくて当然だよ．欲しければとことん努力し，いちいちのめり込まなければ相手に見向きもされないよ．恋愛だって命がけだ．何もしないで指をくわえて見ているだけだったら，単なる無いものねだりだ"
    #text = "最初の話は点をつなぐことについて。"
    text = "私はリード大学を6ヶ月で中退したが、更に1年半ほど後に完全に辞めるまで、もぐりの学生として大学に顔を出していた。ではなぜ中退したのか。"
    print(summarize(text, 'google/pegasus-reddit_tifu'))

if __name__ == "__main__":
    main()
