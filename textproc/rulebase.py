if __package__ is None or __package__ == '':
	import utils
else:
	from . import utils
import re
import spacy

def desmasu2dadearu(text):#ですますをだ・であるに変換
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
	if dic[-1].base_form != "名詞" and wakati[-1] == "か":
		return text
	idx = 0
	for i, token in enumerate(reversed(dic)):
		pos, *_ = token.part_of_speech.split(",")
		base_form = token.base_form
		if pos == "名詞" or base_form == "ない":
			idx = i
			break
	return "".join(wakati[:-idx]) if idx != 0 else text

def sanitize(_doc):
	doc = _doc.copy()
	for i, e in enumerate(doc):
		doc[i] = e.strip()
	return sorted(set(doc), key=doc.index)

def simplify(text):
	text = text.split('、')
	return text[-1]	

def titleize(text, is_extract_subject=True):
	text = simplify(text)
	text = taigendomize(text)
	text = desmasu2dadearu(text)
	if is_extract_subject:
		text = extract_subject(text)
	return text

def extract_subject(text):
	wakati, subject = detect_subject_idx(text)
	print(subject)
	if subject == []:
		return text
	else:
		border = subject[-1]
		return "".join(wakati[:border + 1])

def detect_subject_idx(text):
	parser = spacy.load("ja_ginza")
	doc = parser(text)
	tokens = []
	for sent in doc.sents:
		for token in sent:
			tokens.append(token)
	wakati = []
	subject = []
	for token in tokens:
		wakati.append(token.orth_)
		if token.dep_ in ["nsubj", "nsubjpass", "iobj"]:
			subject.append(token.i)
	return wakati, subject

