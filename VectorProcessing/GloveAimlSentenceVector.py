from VectorProcessing.GloveWordVector import GloveWordVector
from DataPreprocessing.Vocab import get_lexicon
import os
import cPickle as pic
import io
import numpy as np
from sklearn.preprocessing import OneHotEncoder

class GloveAimlSentenceVector():

    def __init__(self, path, training = True, dir = False, dimension = 100, glove_file_path = False, save_word2vec_path = False,
                 save_model_path = False, glove_vocab_file_path = False):
        """
        this class used to create sentence vector
        :param path: give the path of dir or file
        :param dir: False if file is gven
        :param dimension: dimension of glove vector 50,100,200,300
        :param glove_file_path: path of glove vector dir
        :param save_word2vec_path: path of word2vec where it will saved defalut False
        :param save_model_path: path path of saved sen2vec default False
        :param glove_vocab_file_path: path of glove vocab file
        """
        if dir:
            self.dir_path = path
            self.file_path = False
        else:
            self.file_path = path
            self.dir_path = False
        if glove_file_path:
            self.glove_file = glove_file_path
            self.glove_vocab_file = glove_vocab_file_path
        else:
            self.glove_file = '/home/sumit/stanford/glove/vector/glove.6B.'+str(dimension)+'d.txt'

        self.save_model = save_model_path
        self.training = training

        if dir:
            GWV = GloveWordVector(self.dir_path)
        else:
            GWV = GloveWordVector(self.file_path, dir=False)
        if save_word2vec_path:
            with open(save_word2vec_path, 'rb') as f:
                self.word2vec, self.vocab, self.ivocab = pic.load(f)
        else:
            self.word2vec, self.vocab, self.ivocab = GWV.get_glove_word_vector()

    def get_avg_sentenceVector(self, sentence_data):
        sen2vec = []
        if self.training:
            for i in xrange(len(sentence_data)):
                inputs = np.zeros(len(self.word2vec[0]), dtype=float)
                lexicon = get_lexicon(sentence_data[i][0])
                for word in lexicon:
                    inputs += self.word2vec[self.vocab[word]]
                outputs = np.zeros(len(self.word2vec[0]), dtype=float)
                lexicon = get_lexicon(sentence_data[i][1])
                for word in lexicon:
                    outputs += self.word2vec[self.vocab[word]]
                sen2vec.append([inputs, outputs])
        else:
            for i in xrange(len(sentence_data)):
                inputs = np.zeros(len(self.word2vec[0]), dtype=float)
                lexicon = get_lexicon(sentence_data[i][0])
                for word in lexicon:
                    inputs += self.word2vec[self.vocab[word]]
                sen2vec.append(inputs)
        if self.save_model:
            pic.dump([sen2vec], open(self.save_model+'sen2vec.p', 'wb'))
        return sen2vec

    def get_2D_sentenceVector(self, sentence_data, max=50):
        sen2vec = []
        if self.training:
            for i in xrange(len(sentence_data)):
                inputs = np.zeros([max, len(self.word2vec[0])], dtype=float)
                lexicon = get_lexicon(sentence_data[i][0])
                count = 0
                for word in lexicon:
                    if count < max:
                        inputs[count] = self.word2vec[self.vocab[word]]
                    count += 1
                outputs = np.zeros([max, len(self.word2vec[0])], dtype=float)
                lexicon = get_lexicon(sentence_data[i][1])
                count = 0
                for word in lexicon:
                    if count < max:
                        outputs[count] = self.word2vec[self.vocab[word]]
                    count += 1
                sen2vec.append([inputs, outputs])
        else:
            for i in xrange(len(sentence_data)):
                inputs = np.zeros([max, len(self.word2vec[0])], dtype=float)
                lexicon = get_lexicon(sentence_data[i][0])
                count = 0
                for word in lexicon:
                    if count < max:
                        inputs[count] = self.word2vec[self.vocab[word]]
                    count += 1
                sen2vec.append(inputs)
        if self.save_model:
            pic.dump([sen2vec], open(self.save_model+'sen2vec.p', 'wb'))
        return sen2vec


if __name__ == '__main__':
    Vector_class = GloveAimlSentenceVector('/home/sumit/Desktop/project17/ResumeParser/Data/resume_segments/Level0/',
                                       save_model_path='/home/sumit/Desktop/project17/ResumeParser/Data/resume_segments/Test/')
    sen2vec = Vector_class.get_avg_sentenceVector()
    print len(sen2vec)
