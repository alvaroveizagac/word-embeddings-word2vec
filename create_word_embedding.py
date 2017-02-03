from gensim.models import word2vec
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
 

sentences_twitter = []

with open('/resources/word-embeddings/twitter1_6M.txt', 'r') as f:
    for line in f:
        sentences_twitter.append(line.strip().split())

# word vectors 100 size per word
model = word2vec.Word2Vec(sentences_twitter, size=100) 
model.save('twitter1_6M.model')
model.save_word2vec_format('twitter1_6M_model.bin', binary=True)
model.save_word2vec_format('twitter1_6M.model.txt', binary=False)


