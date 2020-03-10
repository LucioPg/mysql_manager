class MySqlTuple(tuple):
    def __new__(self, field, kind=None, length=None, opts=''):
        return tuple.__new__(MySqlTuple, (field, kind, length, opts))
