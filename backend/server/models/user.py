from mongoengine import Document, StringField, EmbeddedDocumentListField


class User(Document):
    name = StringField(required=True, unique=True)
    email = StringField()

    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email
        }
