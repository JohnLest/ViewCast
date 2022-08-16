from tools.genericRepository.genericRepo import GenericRepo


class MediaRepo(GenericRepo):
    def __init__(self, session, table):
        GenericRepo.__init__(self, session, table)
