'''
Knowledge representation

------------------------------------------------------------------------------
SketchNet
Iulius Curt @ 2013
------------------------------------------------------------------------------
'''


class SketchKnowledgeBase(object):
    '''
    SketchKnowledgeBase
    '''
    def __init__(self):
        super(SketchKnowledgeBase, self).__init__()
        self.entities = {}
        self.relations = {}
        # Reversed IS-A relations
        self.asi = {}

        self._idcounter = {}

    def add_entity(self, entity):
        self.entities[entity.name] = entity
        for p in entity.isa:
            if p in self.asi:
                self.asi[p].append(entity.name)
            else:
                self.asi[p] = [entity.name]

    def add_relation(self, rel):
        unqid = self._unique_rel_id(rel.name)
        self.relations[unqid] = rel
        for p in rel.isa:
            punqid = self._unique_rel_id(p)
            if p in self.asi:
                self.asi[punqid].append(unqid)
            else:
                self.asi[punqid] = [unqid]

    def _unique_rel_id(self, relname):
        if relname not in self._idcounter:
            self._idcounter[relname] = -1
        self._idcounter[relname] += 1
        return relname + str(self._idcounter[relname])

    def __str__(self):
        return '(\n  ENTITIES:\n    ' + str(self.entities) + '\n  RELATIONS:\n    ' + str(self.relations) + '\n)\n'


class SNEntity(object):
    '''
    SketchNet Entity
    '''
    def __init__(self, name, sketch, isa=[], partof=[]):
        super(SNEntity, self).__init__()
        self.name, self.sketch, self.isa, self.partof = \
            name, sketch, isa, partof

    def __repr__(self):
        # TODO: strip str(self.isa) of ' characters
        return '<SNE:' + self.name + '::' + str(self.isa) + '>'

    def __str__(self):
        return self.__repr__()


class SNRelation(object):
    '''
    Relation between 2 or more SketchNet entities
    '''
    def __init__(self, name, components, sketch, isa=[], partof=[]):
        super(SNRelation, self).__init__()
        self.name, self.components, self.sketch, self.isa, self.partof = \
            name, components, sketch, isa, partof

    def __repr__(self):
        # TODO: strip list reprs of ' characters
        return '<SNR:' + self.name + '(' + str(self.components)[1:-1] + ')::' + str(self.isa) + '>'

    def __str__(self):
        return self.__repr__()
