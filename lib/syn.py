from nltk.corpus import wordnet
def syn(word):
	syn = wordnet.synsets(word)
	return str(syn[0].lemma_names()[0])
