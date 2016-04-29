from datetime import datetime
from flask.ext.security import UserMixin
import bcrypt

from excuseme import db


class User(db.Document, UserMixin):
    username = db.StringField(required=True, unique=True)
    email = db.StringField(required=True, unique=True)
    name = db.StringField(max_length=255, required=True)
    rating = db.IntField(default=0)
    password = db.StringField(max_length=255, required=True)


class Comment(db.EmbeddedDocument):
    user = db.ReferenceField(User)
    content = db.StringField(nax_length=140, required=True, unique_with='user')
    added = db.DateTimeField(default=datetime.now)


class Excuse(db.Document):
    counter = db.SequenceField(sequence_name='Excuse.counter')
    title = db.StringField(max_length=140, required=True)
    body = db.StringField(max_length=1945, required=True, unique_with='title')
    author = db.ReferenceField(User)
    yes = db.IntField(default=0)
    no = db.IntField(default=0)
    added = db.DateTimeField(default=datetime.now)
    modified = db.DateTimeField(default=datetime.now)
    comments = db.ListField(db.EmbeddedDocumentField(Comment))

    @classmethod
    def vote(cls, excuse, choice=True):
        if choice:
            cls.objects(id=excuse.id).update_one(inc__yes=1)
        else:
            cls.objects(id=excuse.id).update_one(inc__no=1)
        excuse.reload()

    @classmethod
    def add_comment(cls, excuse, comment):
        cls.objects(id=excuse.id).update_one(push__comments=comment)
        excuse.reload()
