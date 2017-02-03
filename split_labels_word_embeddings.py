from gensim.models import word2vec
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


with open("twitter1_6M.model.txt", "r") as lines:
    with open("twitter1_6M_vectors.txt", "a") as f:
        for line in lines:
            linea = line.split()[1:]            
            f.write(' '.join(linea)+"\n")
			
with open("twitter1_6M.model.txt", "r") as lines:
    with open("twitter1_6M_labels.txt", "a") as f:
        for line in lines:
            linea = line.split()[0]            
            f.write(linea+"\n")