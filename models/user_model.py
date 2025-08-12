class UserModel:
    def __init__(self, id=None, name=None, email=None, password=None):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email
        }
