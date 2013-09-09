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
        self.actions = {}
        # Reversed IS-A actions
        self.asi = {}

        self._idcounter = {}

    def add_entity(self, entity):
        self.entities[entity.name] = entity
        for p in entity.isa:
            if p in self.asi:
                self.asi[p].append(entity.name)
            else:
                self.asi[p] = [entity.name]

    def add_action(self, act):
        unqid = self._unique_act_id(act.name)
        self.actions[unqid] = act
        for p in act.isa:
            punqid = self._unique_act_id(p)
            if p in self.asi:
                self.asi[punqid].append(unqid)
            else:
                self.asi[punqid] = [unqid]

    def _unique_act_id(self, actname):
        if actname not in self._idcounter:
            self._idcounter[actname] = -1
        self._idcounter[actname] += 1
        return actname + str(self._idcounter[actname])

    def __str__(self):
        return '(\n  ENTITIES:\n    ' + str(self.entities) + '\n  ACTIONS:\n    ' + str(self.actions) + '\n)\n'


class SNEntity(object):
    '''
    SketchNet Entity
    '''
    def __init__(self, name, sketch, isa=[], partof=[]):
        super(SNEntity, self).__init__()
        self.name, self.sketch, self.isa, self.partof = \
            name, sketch, isa, partof

    def __repr__(self):
        # Strips str(self.isa) of ' characters
        return '<SNE:' + self.name + '::' + str(self.isa).replace("'", "") + '>'

    def __str__(self):
        return self.__repr__()


class SNAction(object):
    '''
    Action over SketchNet entities
    '''
    def __init__(self, name, components, sketch, isa=[], partof=[]):
        super(SNAction, self).__init__()
        self.name, self.components, self.sketch, self.isa, self.partof = \
            name, components, sketch, isa, partof

    def __repr__(self):
        # Strips list reprs of ' characters
        return '<SNR:' + self.name + '(' + str(self.components)[1:-1].replace("'", "") + ')::' + str(self.isa).replace("'", "") + '>'

    def __str__(self):
        return self.__repr__()
