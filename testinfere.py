'''
Unpickle a small test knowledge base and do a little demo inference

------------------------------------------------------------------------------
SketchNet
Iulius Curt @ 2013
------------------------------------------------------------------------------
'''

from knowledge_repr import *


import svgfig
import cPickle as pickle


if __name__ == '__main__':
    # UnPickle the knowledge base
    with open('testkb.pkl', 'rb') as pf:
        kb = pickle.load(pf)

    print kb

    fig1 = svgfig.load('d1.svg')
    fig2 = svgfig.load('d2.svg')

    print fig1[1], fig2[1]
    fig1.append(fig2[1])

    fig1.inkview()
