'''
Unpickle a small test knowledge base and do a little demo inference

------------------------------------------------------------------------------
SketchNet
Iulius Curt @ 2013
------------------------------------------------------------------------------
'''

from knowledge_repr import *
from svghelpers import *


import cPickle as pickle


def mount(action, entities):
    assert len(action.components) == len(entities)
    # TODO: mount each entity in it's spot on the action sketch


if __name__ == '__main__':
    # UnPickle the knowledge base
    with open('testkb.pkl', 'rb') as pf:
        kb = pickle.load(pf)

    print kb

    fig1 = load_sketch('mpt1')
    fig2 = load_sketch('mpt2')

    regfig = register_sketches('mpt1', fig1, 'mpt2', fig2)

    # Save generated SVG file
    regfig.save("fig_final.svg")
