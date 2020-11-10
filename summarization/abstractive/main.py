import summarizer
import translater

def main(text):
    ag = summarizer.Pegasus()
    trans = translater.DeepLTransltator()

    src = text
    trc = trans.translate_to_en(src)
    print(trc)
    strc = ag.exec(trc)
    print(strc)
    result = trans.translate_to_ja(strc)
    print(result)

if __name__ == "__main__":
    text = "おしゃべりであることは、とくに工学の研究者にとって非常に大切である。日本語でも英語もおしゃべりであること。英語力はしゃべりたがり度のバロメーターである。研究能力は高校の現代国語の成績に強い相関を持つという。海外に出よ。休みを取ってヨーロッパを旅せよ。絶対に２人以上で行くな。必ず１人で行かなければ、大金をドブに捨てるようなものだ。しゃべることは人間の基本であり、場を持たせることは思いやりの心そのものである。沈黙は禁なり。ろくな研究もしていないのに、しゃべりだけでがんばる人もいるが、それはいずれはボロが出る。しかし、しゃべらないことには何にも生まれない。研究者は、強い説得力を持つことが絶対必要である。相手に面と向って自分の意見を述べ、相手の意見を聞いて議論しよう。毎日電子掲示板（今はホームページか）を読んでニヤニヤしている君、ちゃんと人間と話していますか？"
    main(text)