'''
Generate small test data and pickle it

------------------------------------------------------------------------------
SketchNet
Iulius Curt @ 2013
------------------------------------------------------------------------------
'''

from knowledge_repr import *

import cPickle as pickle


if __name__ == '__main__':
    kb = SketchKnowledgeBase()

    # ---------------------------------------------------
    # Entities
    # ---------------------------------------------------

    # FLYING-THING
    kb.add_entity(SNEntity(
                name='flying-thing',
                sketch='',
                isa=['thing']
            )
        )

    # BIRD
    kb.add_entity(SNEntity(
                name='bird',
                sketch='',
                isa=['flying-thing', 'animal']
            )
        )

    # OBSTACLE
    kb.add_entity(SNEntity(
                name='obstacle',
                sketch='',
                isa=['thing']
            )
        )

    # WALL
    kb.add_entity(SNEntity(
                name='wall',
                sketch='',
                isa=['obstacle']
            )
        )

    # ---------------------------------------------------
    # Relations
    # ---------------------------------------------------

    # FLYING-CRASH(flying-thing, obstacle)
    kb.add_relation(SNRelation(
                name='flying-crash',
                components=['flying-thing', 'obstacle'],
                sketch='',
                isa=['crash']
            )
        )

    # FLYING-CRASH(flying-thing, flying-thing)
    kb.add_relation(SNRelation(
                name='flying-crash',
                components=['flying-thing', 'flying-thing'],
                sketch='',
                isa=['crash']
            )
        )

    print kb

    # Pickle the knowledge base
    with open('testkb.pkl', 'wb') as pf:
        pickle.dump(kb, pf, protocol=pickle.HIGHEST_PROTOCOL)
