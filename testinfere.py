'''
Unpickle a small test knowledge base and do a little demo inference

------------------------------------------------------------------------------
SketchNet
Iulius Curt @ 2013
------------------------------------------------------------------------------
'''

from knowledge_repr import *

import cPickle as pickle


if __name__ == '__main__':
    # UnPickle the knowledge base
    with open('testkb.pkl', 'rb') as pf:
        kb = pickle.load(pf)

    print kb
