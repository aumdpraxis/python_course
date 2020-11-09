"""
contains:
    class: KnnRecommender
"""

import pandas as pd 
import numpy as np 

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import warnings
warnings.filterwarnings('ignore')

class WordVectRecommender:

    _data = None
    _target_column = None
    _title_column = None
    _max_size = None
    _cosine_sim = None
    _indices = None

    def __init__(self,target='description',title='title',max_row=5000):
        self._target_column = target
        self._title_column = title
        self._max_size = max_row

    def train(self,data_frame):
        ## DATAFRAME TREATMENT
        self._data = data_frame
        self._data = self._data.head(self._max_size)
        self._data[self._target_column] = self._data[self._target_column].fillna('')
        
        ## GET INDIEX cross NAMES matrix
        self._indices = pd.Series( self._data.index, index=self._data[self._title_column] ).drop_duplicates()
        
        ## MODEL INIT AND TRAIN
        _tfidf = TfidfVectorizer( stop_words='english' )
        _tfidf_matrix = _tfidf.fit_transform( self._data[self._target_column] )

        ## GET DISTANCES BETWEEN OBJECTS MODEL
        self._cosine_sim = cosine_similarity( _tfidf_matrix, _tfidf_matrix )
    
    def recommend(self,title,num_recommendations):
        ## GET ITEM ON DATA_BASE
        idx = self._indices[title]

        ## getting the most similar items
        if type( self._cosine_sim[idx] )!='numpy.float64' :
            sim_scores = list( enumerate(self._cosine_sim[idx]) )
        else:
            sim_scores = list( (0,self._cosine_sim[idx] ) )
        
        ## if SIMS_SCORES is a vector or not( repeated items in database, or repeated names )
        if type(sim_scores[1])=='numpy.float64':
            ## reordering items by similarity
            sim_scores = sorted( sim_scores,key=lambda x:x[1], reverse=True )
        else:
            sim_scores = sorted( sim_scores,key=lambda x:np.linalg.norm(x[1]), reverse=True )

        ## slicing for onli desired items
        sim_scores = sim_scores[1:num_recommendations]
        item_indices = [i[0] for i in sim_scores]

        ## RESULTS
        return self._data.iloc[item_indices]