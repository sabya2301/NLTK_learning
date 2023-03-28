# import nltk

# print("nltk download start------")
# nltk.download
# print("nltk download complete-----")
########################################################################################################################

# from nltk.tokenize import sent_tokenize as sentence_tokenize, word_tokenize
# sentence = "Hello, this is a demo NLTK project. I am Mr. Das. Lets try something today! have a nice day. bye!   :)"
#
# print("printing sent_tokenize....")
# print(sentence_tokenize(sentence))
#
# print("\n\nprinting word_tokenize...")
# print(word_tokenize(sentence))

########################################################################################################################

# from nltk.corpus import stopwords
# from nltk.tokenize import sent_tokenize, word_tokenize
#
# example_words = "this is a demo sentence."
# stop_words = stopwords.words("english")
# # print(stop_words)
# # print(set(stop_words))
#
# sentence_without_stop_words = [w for w in word_tokenize(example_words) if not w in set(stop_words)]
# print(sentence_without_stop_words)

########################################################################################################################

from nltk.stem import PorterStemmer
#
# ps = PorterStemmer()
# example_words = ["has", "have", "had", "haven't"]
#
# stemmed_words = [ps.stem(w) for w in example_words]
# print(stemmed_words)

########################################################################################################################

