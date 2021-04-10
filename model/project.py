from sys import maxsize

class Project:

    def __init__(self, id=None, name=None, desc=None):
        self.id = id
        self.name = name
        self.desc = desc

    def __repr__(self):
        return "id=%s name=%s desc=%s" % (self.id, self.name, self.desc)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and (self.name == other.name)

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
