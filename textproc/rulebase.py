from . import utils

def desumasu(text):#ですますをだ・であるに変換
    """
    wakati,dic= utils.wakatize(text)
    for i in range(len(wakati)):
        if wakati[i] in ["です","ます"]:
            wakati[i]={"です":"だ","ます":"た"}[wakati[i]]
    return ''.join(wakati)
    """
    chikan_list=[['しましょう','しよう'],
            ['きましょう','こう'],
			['りましょう','ろう'],
			['出来ました','出来た'],
			['できました','できた'],
			['出来ます','出来る'],
			['できます','できる'],
			['あります','ある'],
			['なります','なる'],
			['きました','くる'],
			['ませんが','ないが'],
			['でしょう','だろう'],
			['りません','らない'],
			['みました','みた'],
			['ましょう','よう'],
			['でした','だった'],
			['ですが','だが'],
			['います','いる'],
			['かります','かる'],
			['えました','えた'],
			['いいです','いい'],
			['ないです','ない'],
			['無いです','無い'],
			['れます','れる'],
			['きます','くる'],
			['します','する'],
			['します','する'],
			['ません','ない'],
			['ていた','いた'],
			['ました','た'],
			['ります','る'],
			['ます','る'],
			['です','だ']]
    for chikan in chikan_list:
        text=text.replace(chikan[0],chikan[1])
    return text

def taigendomize(text):
    wakati, dic = utils.wakatize(text)
    idx = 0
    for i, token in enumerate(reversed(dic)):
        pos, *_ = token.part_of_speech.split(",")
        if pos == "名詞":
            idx = i
            break
    return "".join(wakati[:-idx])

def seq2se2noise_sanitize(doc):
    return sorted(set(doc), key=doc.index)
