class Channel:

    @classmethod
    def from_payload(cls, payload): return cls(**payload)

    def __init__(self, **kwargs):
        self.id = kwargs.get('id')
        self.name = kwargs.get('name')
        self.type = kwargs.get('type')
        self.position = kwargs.get('position')
        self.permission_overwrites = kwargs.get('permission_overwrites')

