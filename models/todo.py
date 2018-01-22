from utils import log
from models import Model
import time

class Todo(Model):

    @classmethod
    def update(cls, id, form):
        t = cls.find_by(id=id)
        valid_names = [
            'title',
            'completed'
        ]
        for key in valid_names:
            setattr(t, key, form[key])
        t.save()
        return t

    def __init__(self, form):
        self.id = None
        self.title = form.get('title', '')
        self.completed = False
        self.ct = int(time.time())
        self.ut = self.ct

