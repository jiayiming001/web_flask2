import  json
from utils import log

def load(path):
    with open(path, 'r', encoding='utf-8') as f:
        f = f.read()
        #log('log load', s)
    return json.loads(f)


def save(data, path):
    s = json.dumps(data, indent=2, ensure_ascii=False)
    with open(path, 'w+', encoding='utf-8') as f:
       # log('save', path, s, data)
        f.write(s)


class Model(object):


    @classmethod
    def db_path(cls):
        classname = cls.__name__
        path = 'data/{}.txt'.format(classname)
        return path

    @classmethod
    def new(cls, form):
        m = cls(form)
        return m

    @classmethod
    def _new_form_dict(cls, d):
        m = cls({})
        for k, v in d.items():
            setattr(m,k,v)
        return m

    @classmethod
    def all(cls):
        path = cls.db_path()
        models = load(path)
        ms = [cls._new_form_dict(m) for m in models]
        return ms

    @classmethod
    def find_by(cls,**kwargs):
        ms = cls.all()
        for m in ms:
            for k, v in kwargs.items():
                if hasattr(m, k) and getattr(m, k) == v:
                    return m
        return None


    @classmethod
    def find_all(cls, **kwargs):
        ms = cls.all()
        l = []
        for m in ms:
            for k, v in kwargs.items():
                if hasattr(m, k) and getattr(m, k) == v:
                    l.append(m)
        return l


    @classmethod
    def delete(cls, id):
        models = cls.all()
        index = -1
        for i, m in enumerate(models):
            if m.id == id:
                index = i
                break

        if index == -1:
            pass
        else:
            obj = models.pop(index)
            l = [m.__dict__ for m in models]
            path = cls.db_path()
            save(l, path)
            return obj


    def  save_register_id(self, models):
        first_index = 0
        if self.__dict__.get('id') is None:
            if len(models) > 0:
                self.id = models[-1].id + 1
            else:
                self.id = first_index
            models.append(self)
        else:
            index = -1
            for i, m in enumerate(models):
                if m.id == self.id:
                    index = i
                    break
            if index > -1:
                models[index] = self
        return models


    def save(self):
        models = self.all()
        models = self.save_register_id(models)
        l = [m.__dict__ for m in models]
        path = self.db_path()
        save(l, path)


    def  remove(self):
        models = self.all()
        if self.__dict__.get('id') is  not None:
            index = -1
        for i, m in enumerate(models):
            if m.id == self.id:
                index = i
                break
        if index > -1:
            del models[index]
        l = [m.__dict__ for m in models]
        path = self.db_path()
        save(l, path)


    def json(self):
        return self.__dict__.copy()

    def __repr__(self):
        classname = self.__class__.__name__
        properties = ['{}: ({})'.format(k, v) for k, v in self.__dict__.items()]
        s = '\n'.join(properties)
        return '< {}\n{} >\n'.format(classname, s)


