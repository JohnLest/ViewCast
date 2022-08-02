from tools.genericRepository.genericRepo import GenericRepo


class FluxDataRepo(GenericRepo):
    def __init__(self, session, table):
        GenericRepo.__init__(self, session, table)
